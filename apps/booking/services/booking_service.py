from apps.booking.booking_state_factory import BookingStateFactory

# from apps.booking.repositories.booking_status_repository import BookingStatusRepository
from apps.booking.constants.const_booking_status import ConstBookingStatus
from apps.booking.exceptions.booking_exists_exception import BookingExistsException
from apps.booking.models.booking import Booking

# from core.base_repository import BaseRepository
from core.base_service import BaseService


class BookingService(BaseService[Booking]):
    # def __init__(self, rep: BaseRepository, booking_status_rep: BookingStatusRepository):
    #     super().__init__(rep)
    #     self._booking_status_rep = booking_status_rep

    def get_related(self, **filters):
        bookings = super().get(**filters)
        return bookings.select_related("hotel_room", "hotel_room__type", "status")

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

        return super().update(obj_id, **validation_data)

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
