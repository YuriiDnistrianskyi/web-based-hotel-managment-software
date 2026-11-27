from decimal import Decimal

from django.db import transaction

from apps.booking.booking_state_factory import BookingStateFactory
from apps.booking.calculators.calculator_manager import CalculatorManager
from apps.booking.constants.const_booking_status import ConstBookingStatus
from apps.booking.exceptions.booking_exists_exception import BookingExistsException
from apps.booking.models.booking import Booking
from apps.booking.repositories.booking_status_repository import BookingStatusRepository
from apps.booking.repositories.booking_to_service_repository import (
    BookingToServiceRepository,
)
from apps.hotel_room.models.hotel_room import HotelRoom
from apps.hotel_room.repositories.hotel_room_repository import HotelRoomRepository
from core.base_repository import BaseRepository
from core.base_service import BaseService


class BookingService(BaseService[Booking]):
    def __init__(self, 
        rep: BaseRepository, 
        booking_status_rep: BookingStatusRepository, 
        booking_to_service_rep: BookingToServiceRepository,
        hotel_room_rep: HotelRoomRepository
    ):
        super().__init__(rep)
        self._booking_status_rep = booking_status_rep
        self._booking_to_service_rep = booking_to_service_rep
        self._hotel_room_rep = hotel_room_rep

    def get_related(self, **filters):
        bookings = super().get(**filters)
        return bookings.select_related("hotel_room", "hotel_room__type", "status") #?

    @transaction.atomic
    def create(self, **validation_data):
        check_in = validation_data.get('check_in')
        check_out = validation_data.get('check_out')
        number_of_guests = validation_data.get('number_of_guests')
        hotel_room = validation_data.get('hotel_room')

        busy_booking = self._rep.get(
            status__title__in=[ConstBookingStatus.CONFIRMED, ConstBookingStatus.INPROGRESS],
            check_in__lt=check_out,
            check_out__gt=check_in,
            hotel_room__id=hotel_room.id,
        )

        if busy_booking.exists():
            raise BookingExistsException("This room is already booked for there dates")

        services = validation_data.pop('services', [])
        validation_data['status'] = self._booking_status_rep.get_by_title(ConstBookingStatus.CONFIRMED)
        validation_data['price'] = self.calculate(
            services=services, 
            hotel_room_id=hotel_room.id,
            dates=(check_in, check_out),
            number_of_guests=number_of_guests
        )
        result = super().create(**validation_data)

        additional_data = {
                'check_in': check_in,
                'check_out': check_out,
                'number_of_guests': number_of_guests
            }
        for service in services:
            price = CalculatorManager.calculate(service=service, **additional_data)
            self._booking_to_service_rep.create(
                booking=result,
                service=service,
                price=price
            )

        return result

    @transaction.atomic
    def update(self, obj_id, **validation_data):
        obj = self._rep.get_by_id(obj_id)

        check_in = validation_data.get("check_in", obj.check_in)
        check_out = validation_data.get("check_out", obj.check_out)

        busy_bookings = self._rep.get(
            status__title__in=[ConstBookingStatus.CONFIRMED, ConstBookingStatus.INPROGRESS],
            check_in__lt=check_in,
            check_out__gt=check_out,
            hotel_room__id=obj.hotel_room_id
        ).exclude(id=obj_id)

        if busy_bookings.exists():
            raise BookingExistsException("This room is already booked for there dates")

        services = validation_data.pop('services', [])
        new_price = self.calculate(hotel_room_id=obj.hotel_room_id, obj_id=obj_id, services=services)
        validation_data["price"] = new_price
        result = super().update(obj_id, **validation_data)

        self._booking_to_service_rep.delete_by_booking_id(obj_id=obj_id)
        additional_data = {
            'check_in': check_in,
            'check_out': check_out,
            'number_of_guests': validation_data.get('number_of_guests')
        }
        for service in services:
            price = CalculatorManager.calculate(service=service, booking=result, **additional_data)
            self._booking_to_service_rep.create(
                booking=result,
                service=service,
                price = price
            )

        return result

    def calculate(self, 
        services: list, 
        hotel_room_id: HotelRoom,
        obj_id: int | None=None,
        dates: list | None=None, 
        number_of_guests: int | None=None
    ) -> float:
        obj = self._rep.get_by_id(obj_id=obj_id) if obj_id else None

        if dates:
            check_in, check_out = dates
        elif obj:
            check_in, check_out = (obj.check_in, obj.check_out)
        else:
            return 0.0

        if not number_of_guests:
            if obj:
                number_of_guests = obj.number_of_guests
            else:
                return 0

        days = (check_out - check_in).days
        hotel_room = self._hotel_room_rep.get_by_id(hotel_room_id)

        price = Decimal('0.00')
        price += hotel_room.price * days

        additional_date = {
            'check_in': check_in,
            'check_out': check_out,
            'number_of_guests': number_of_guests
        }

        for service in services:
            service_price = CalculatorManager.calculate(
                service=service,
                booking=obj,
                **additional_date,
            )
            price += service_price

        return price

    def start_booking(self, obj_id: int):
        booking = self._rep.get_by_id(id=obj_id)

        state = BookingStateFactory.create(booking)
        state.start(booking)

        return self._rep.update(booking)

    def complete_booking(self, obj_id: int):
        booking = self._rep.get_by_id(obj_id)
        
        state = BookingStateFactory.create(booking)
        state.complete(booking)
        
        return self._rep.update(booking)

    def cancel_booking(self, obj_id: int):
        booking = self._rep.get_by_id(obj_id)
        
        state = BookingStateFactory.create(booking)
        state.cancel(booking)
        
        return self._rep.update(booking)
