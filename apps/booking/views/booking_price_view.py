import json
from datetime import date

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from apps.booking.services import booking_service, service_service


@login_required
@require_POST
def booking_price(request, booking_id):
    data = json.loads(request.body)
    services = [
        service_service.get_by_id(int(str_id)) 
        for str_id in data.get('services', [])
    ]

    price = booking_service.calculate(
        booking_id, 
        dates= [
            date.fromisoformat(data.get('check_in')),
            date.fromisoformat(data.get('check_out'))
        ],
        number_of_guests=int(data.get('number_of_guests')),
        services=services
    )

    return JsonResponse({
        'price': price
    })
