from abc import ABC

from apps.booking.models.booking import Booking


class BaseState(ABC):
    def start(self, booking: Booking):
        pass

    def complet(self, booknig: Booking):
        pass

    def cancel(self, booking: Booking):
        pass
