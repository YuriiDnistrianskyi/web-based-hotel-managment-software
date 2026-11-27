from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.booking.constants.const_booking_status import ConstBookingStatus
from apps.booking.services import booking_service
from apps.user.constants import ConstUserRole
from apps.user.role_required import role_required


@login_required
@role_required(ConstUserRole.USER)
def user_account_view(request):
    bookings = booking_service.get(
        user=request.user,
        status__title=ConstBookingStatus.COMPLETED
    ).count()

    return render(request, "user/account.html", {
        "successful_bookings" : bookings
    })
