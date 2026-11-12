from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.booking.models.booking import Booking
from apps.booking.services import booking_service


class HistoryView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/history.html'
    context_object_name = 'bookings'
    paginate_by = 10
    ordering = ['status__id', '-check_in']

    def get_queryset(self):
        bookings = booking_service.get_related(user_id=self.request.user.id)
        return bookings 
