from abc import ABC

from apps.booking.exceptions.booking_state_exception import BookingStateException
from apps.booking.models.booking import Booking


class BaseState(ABC):
    def start(self, booking: Booking):
        raise BookingStateException(f"Can't start booking: {booking.id}")

    def complet(self, booking: Booking):
        raise BookingStateException(f"Can't complete booking: {booking.id}")

    def cancel(self, booking: Booking):
        raise BookingStateException(f"Can't cancel booking: {booking.id}")
