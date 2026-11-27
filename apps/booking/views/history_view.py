from django.views.generic import ListView

from apps.booking.models.booking import Booking
from apps.booking.services import booking_service
from apps.user.mixins import UserRequiredMixin


class HistoryView(UserRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/history.html'
    context_object_name = 'bookings'
    paginate_by = 10
    ordering = ['status__id', '-check_in']

    def get_queryset(self):
        bookings = booking_service.get_related(user_id=self.request.user.id).prefetch_related("services")
        return bookings.order_by(*self.ordering)
