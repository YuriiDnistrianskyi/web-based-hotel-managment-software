from .constants.const_booking_status import ConstBookingStatus
from .models.booking import Booking
from .repositories import booking_status_rep
from .state import (
    BaseState,
    CanceledState,
    CompletedState,
    ConfirmedState,
    InProgressState,
)


class BookingStateFactory:
    @staticmethod
    def create(booking: Booking) -> BaseState:
        states = {
            ConstBookingStatus.CONFIRMED: ConfirmedState,
            ConstBookingStatus.INPROGRESS: InProgressState,
            ConstBookingStatus.COMPLETED: CompletedState,
            ConstBookingStatus.CANCELLED: CanceledState # ?
        }

        status_title = booking_status_rep.get_by_id(booking.status_id).title
        state = states.get(status_title)

        if state is None:
            raise ValueError(f"Uknow booking status: {status_title}")

        return state
