import logging
from decimal import Decimal

from apps.booking.models import Booking, Service

from .by_guests_by_days_calculator import ByGuestsByDaysCalculator
from .one_time_calculator import OneTimeCalculator

logger = logging.getLogger(__name__)


class CalculatorManager:
    CALCULATORS = {
        'Meals': ByGuestsByDaysCalculator,
        'Transfer': OneTimeCalculator,
        'SPA': OneTimeCalculator
    }

    @classmethod
    def calculate(cls, booking: Booking, service: Service, **additional_data) -> Decimal:
        price = Decimal('0.00')

        calculator_class = cls.CALCULATORS.get(service.title)
        if calculator_class:
            calculator = calculator_class()
            price += calculator.calculate(booking, service, **additional_data)
        else:
            logger.error(f"Unknow service title in CALCULATORS: {service.title}")

        return price
