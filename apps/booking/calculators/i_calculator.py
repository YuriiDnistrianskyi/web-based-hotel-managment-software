from abc import ABC, abstractmethod
from decimal import Decimal

from apps.booking.models import Booking, Service


class ICalculator(ABC):
    @abstractmethod
    def calculate(self, service: Service, booking: Booking=None, **additional_data) -> Decimal:
        pass
