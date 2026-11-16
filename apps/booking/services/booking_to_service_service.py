# from apps.booking.models.booking_to_service import BookingToService
from apps.booking.models.booking import Booking
from apps.booking.models.service import Service
from apps.booking.repositories.booking_to_service_repository import (
    BookingToServiceRepository,
)


class BookingToServiceService:
    def __init__(self, rep: BookingToServiceRepository):
        self._rep = rep

    def get_by_booking_id(self, booking_id: int):
        return self._rep.get_by_booking_id(booking_id=booking_id)

    def get_by_service_id(self, service_id: int):
        return self._rep.get_by_service_id(booking_id=service_id)

    def add_service(self, booking: Booking, service: Service):
        return self._rep.create(
            booking=booking,
            service=service
        )
