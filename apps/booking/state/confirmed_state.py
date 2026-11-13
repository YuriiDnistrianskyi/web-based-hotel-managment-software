from apps.booking.constants.const_booking_status import ConstBookingStatus
from apps.booking.models.booking import Booking
from apps.booking.repositories import booking_status_rep

from .base_state import BaseState


class ConfirmedState(BaseState):
    def start(booking: Booking):
        booking.status = booking_status_rep.get_by_title(
            title = ConstBookingStatus.INPROGRESS
        )

    def cancel(booking: Booking):
        booking.status = booking_status_rep.get_ty_title(
            title= ConstBookingStatus.CANCELLED
        )
