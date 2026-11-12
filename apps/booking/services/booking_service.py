from apps.booking.models.booking import Booking
from core.base_service import BaseService


class BookingService(BaseService[Booking]):
    def get_related(self, **filters):
        bookings = super().get(**filters)
        return bookings.select_related("hotel_room", "hotel_room__type", "status")
