from decimal import Decimal

from apps.booking.models import Booking, Service

from .i_calculator import ICalculator


class OneTimeCalculator(ICalculator):
    def calculate(self, service: Service, booking: Booking=None, **additional_data) -> Decimal:
        return service.price
