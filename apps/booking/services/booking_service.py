from apps.booking.booking_state_factory import BookingStateFactory
from apps.booking.models.booking import Booking
from core.base_service import BaseService


class BookingService(BaseService[Booking]):
    def get_related(self, **filters):
        bookings = super().get(**filters)
        return bookings.select_related("hotel_room", "hotel_room__type", "status")

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
        booking = self._rep.get_by_id(id=obj_id)
        
        state = BookingStateFactory.create(booking)
        state.cancel(booking)
        
        return self._rep.update(booking)
