from decimal import Decimal

from apps.booking.booking_state_factory import BookingStateFactory
from apps.booking.calculators.calculator_manager import CalculatorManager
from apps.booking.constants.const_booking_status import ConstBookingStatus
from apps.booking.exceptions.booking_exists_exception import BookingExistsException
from apps.booking.models.booking import Booking
from apps.booking.repositories.booking_to_service_repository import (
    BookingToServiceRepository,
)
from core.base_repository import BaseRepository
from core.base_service import BaseService


class BookingService(BaseService[Booking]):
    def __init__(self, rep: BaseRepository, booking_to_service_rep: BookingToServiceRepository):
        super().__init__(rep)
        self._booking_to_service_rep = booking_to_service_rep

    def get_related(self, **filters):
        bookings = super().get(**filters)
        return bookings.select_related("hotel_room", "hotel_room__type", "status") #?

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

        services = validation_data.get("services", [])
        self._booking_to_service_rep.delete_by_booking_id(obj_id=obj_id)
        for service in services:
            price = CalculatorManager.calculate(obj, service)
            self._booking_to_service_rep.create(
                booking=obj,
                service=service,
                price = price
            )

        new_price = self.calculate(obj_id=obj_id, services=services)
        validation_data["price"] = new_price

        validation_data.pop('services')

        return super().update(obj_id, **validation_data)

    def calculate(self, obj_id: int, services: list, dates: list | None=None, number_of_guests: int | None=None) -> float:
        obj = self._rep.get_by_id(obj_id=obj_id)

        price = Decimal('0.00')
        if dates:
            check_in, check_out = dates
        else:
            check_in, check_out = (obj.check_in, obj.check_out)

        if not number_of_guests:
            number_of_guests = obj.number_of_guests

        days = (check_out - check_in).days
        price += obj.hotel_room.price * days

        additional_date = {
            'check_in': check_in,
            'check_out': check_out,
            'number_of_guests': number_of_guests
        }

        for service in services:
            service_price = CalculatorManager.calculate(
                obj, 
                service,
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
