# from booking.models.booking import Booking
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.dateparse import parse_date
from django.views.generic import ListView

from apps.hotel_room.constants.const_room_type import ConstRoomType
from apps.hotel_room.constants.const_room_status import ConstRoomStatus
from apps.hotel_room.models.hotel_room import HotelRoom
from apps.hotel_room.services import hotel_room_service


class HomeView(LoginRequiredMixin, ListView):
    model = HotelRoom
    template_name = 'hotel_room/home.html'
    context_object_name = 'rooms'
    paginate_by = 12

    def _parse_int(self, value: str):
        try:
            value = int(value)
            return value
        except ValueError:
            return None

    def _parse_date(self, value: str):
        try:
            value = parse_date(value)
            return value
        except ValueError:
            return None

    def get_filters(self):
        check_in = self._parse_date(self.request.GET.get("check_in", ""))
        check_out = self._parse_date(self.request.GET.get("check_out", ""))
        if check_in is None or check_out is None or check_in >= check_out:
            check_in = check_out = None

        filters = {
                "check_in": check_in,
                "check_out": check_out,
                "type": self.request.GET.get("room_type"),
                "capacity": self._parse_int(self.request.GET.get("capacity", "")),
                "price_max": self._parse_int(self.request.GET.get("price_max", "")),
                "status": ConstRoomStatus.VACANT
            }

        return {k: v for k, v in filters.items() if v is not None}

    def get_queryset(self):
        filters = self.get_filters()
        rooms = hotel_room_service.get(**filters)
        return rooms

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["room_types"] = ConstRoomType.TYPES
        context["capacities"] = range(1, 6)
        return context
