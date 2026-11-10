# from booking.models.booking import Booking
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.dateparse import parse_date
from django.views.generic import ListView

from apps.hotel_room.models.hotel_room import HotelRoom
from apps.hotel_room.services import hotel_room_service


class HomeView(LoginRequiredMixin, ListView):
    model = HotelRoom
    template_name = 'hotel_room/home.html'
    context_object_name = 'rooms'
    paginate_by = 12

    def get_filters(self):
        try:
            check_in = parse_date(self.request.GET.get("check_in", ""))
            check_out = parse_date(self.request.GET.get("check_out", ""))
            room_type = self.request.GET.get("room_type", "")
            capacity = int(self.request.GET.get("capacity", ""))
            price_min = int(self.request.GET.get("price_min", ""))
        except ValueError:
            return {}

        if check_in and check_out and check_in >= check_out:
            return {}
        return {
                "check_in": check_in,
                "check_out": check_out,
                "room_type": room_type,
                "capacity": capacity,
                "price_min": price_min
            }

    def get_queryset(self):
        filters = {k: v for k, v in self.get_filters().items() if v is not None and v != ""}
        rooms = hotel_room_service.get(**filters)
        return rooms
