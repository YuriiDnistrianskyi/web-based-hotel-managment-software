from django.views.generic import ListView

from apps.hotel_room.constants.const_room_status import ConstRoomStatus
from apps.hotel_room.constants.const_room_type import ConstRoomType
from apps.hotel_room.models.hotel_room import HotelRoom
from apps.hotel_room.services import hotel_room_service
from apps.user.mixins import AdminRequiredMixin


class RoomsView(AdminRequiredMixin, ListView):
    model = HotelRoom
    template_name = 'dashboard/rooms.html'
    context_object_name = 'rooms'
    paginate_by =  12

    def get_filters(self):
        status = self.request.GET.get('status')
        room_type = self.request.GET.get('type')
        return {
            'status': status,
            'type': room_type,
        }

    def get_queryset(self):
        filters = self.get_filters()
        rooms = hotel_room_service.get(**filters)
        return rooms
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "room_statuses": ConstRoomStatus.TYPES,
            "room_types": ConstRoomType.TYPES,
            "room_status": self.request.GET.get('status', ''),
            "room_type": self.request.GET.get('type', ''),
        })
        return context
