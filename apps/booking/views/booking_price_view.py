import json
from datetime import date

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from apps.booking.services import booking_service, service_service
from apps.user.constants import ConstUserRole
from apps.user.role_required import role_required


@login_required
@role_required(ConstUserRole.USER)
@require_POST
def booking_price(request, hotel_room_id: int):
    data = json.loads(request.body)
    services = [
        service_service.get_by_id(int(str_id)) 
        for str_id in data.get('services', [])
    ]

    price = booking_service.calculate(
        obj_id=data.get('booking_id'), 
        hotel_room_id=hotel_room_id,
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
