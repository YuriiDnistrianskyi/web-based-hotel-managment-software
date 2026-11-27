from django.views.generic import TemplateView

from apps.booking.constants.const_booking_status import ConstBookingStatus
from apps.booking.services import booking_service
from apps.hotel_room.constants.const_room_status import ConstRoomStatus
from apps.hotel_room.services import hotel_room_service


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['vacant_rooms'] = hotel_room_service.get(status=ConstRoomStatus.VACANT)
        context['occupied_rooms'] = hotel_room_service.get(status=ConstRoomStatus.OCCUPIED)
        context['in_progress_bookings'] = booking_service.get(
            status__title=ConstBookingStatus.INPROGRESS
        ).prefetch_related('services')

        return context
