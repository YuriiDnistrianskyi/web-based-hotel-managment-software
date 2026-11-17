from decimal import Decimal

from apps.booking.models import Booking, Service

from .i_calculator import ICalculator


class ByGuestsByDaysCalculator(ICalculator):
    def calculate(self, booking: Booking, service: Service, **additional_data) -> Decimal:
        guests = additional_data.get('number_of_guests', booking.number_of_guests)
        check_in = additional_data.get('check_in', booking.check_in)
        check_out = additional_data.get('check_out', booking.check_out)
        days = (check_out - check_in).days

        return service.price * guests * days
