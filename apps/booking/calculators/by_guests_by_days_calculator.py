from decimal import Decimal

from apps.booking.models import Booking, Service

from .i_calculator import ICalculator


class ByGuestsByDaysCalculator(ICalculator):
    def calculate(self, service: Service, booking: Booking=None, **additional_data) -> Decimal:
        guests = additional_data.get('number_of_guests')
        check_in = additional_data.get('check_in')
        check_out = additional_data.get('check_out')

        if booking:
            if not guests:
                guests = booking.number_of_guests
            if not check_in:
                check_in = booking.check_in
            if not check_out:
                check_out = booking.check_out 

        days = (check_out - check_in).days

        return service.price * guests * days
