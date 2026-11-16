from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from apps.booking.services import booking_service


@login_required
@require_POST
def cancel_booking(request, booking_id):
    booking_service.cancel_booking(booking_id)

    return redirect("history")
