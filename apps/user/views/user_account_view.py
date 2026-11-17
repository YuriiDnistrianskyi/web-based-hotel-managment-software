from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.booking.constants.const_booking_status import ConstBookingStatus
from apps.booking.services import booking_service


@login_required
def user_account_view(request):
    bookings = booking_service.get(
        user=request.user,
        status__title=ConstBookingStatus.COMPLETED
    ).count()

    return render(request, "user/account.html", {
        "successful_bookings" : bookings
    })
