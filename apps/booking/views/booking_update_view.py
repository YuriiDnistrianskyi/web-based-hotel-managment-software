from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.booking.forms.booking_update_form import BookingUpdateForm
from apps.booking.models.booking import Booking
from apps.booking.services import booking_service


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingUpdateForm
    template_name = 'booking/edit.html'

    def get_query(self):
        return booking_service.get(user_id=self.request.user.id)

    def form_valid(self, form):
        try:
            booking_service.update(
                obj_id=self.object.id,
                check_in=form.cleaned_data['check_in'],
                check_out=form.cleaned_data['check_out'],
                number_of_guests=form.cleaned_data['number_of_guests'],
                services=form.changed_data['services']
            )
    
            return redirect(reverse_lazy('history'))
        except forms.ValidationError as error:
            form.add_error(None, error)
            return self.form_invalid(form)
