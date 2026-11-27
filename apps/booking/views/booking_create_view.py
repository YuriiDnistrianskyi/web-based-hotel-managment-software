from datetime import date, timedelta

from django import forms
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.booking.exceptions.booking_exists_exception import BookingExistsException
from apps.booking.forms.booking_create_form import BookingCreateForm
from apps.booking.services import booking_service
from apps.hotel_room.services import hotel_room_service
from apps.user.mixins import UserRequiredMixin


class BookingCreateView(UserRequiredMixin, FormView):
    form_class = BookingCreateForm
    template_name = 'booking/create.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        self.hotel_room = hotel_room_service.get_by_id(
            obj_id=kwargs['hotel_room_id']
        )

        if not self.hotel_room:
            raise Http404

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotel_room'] = self.hotel_room
        return context

    def get_initial(self):
        initial = super().get_initial()

        today = date.today()
        tomorrow = today + timedelta(days=1)

        initial.update({
            'check_in': self.request.GET.get('check_in', today),
            'check_out': self.request.GET.get('check_out', tomorrow),
            'number_of_guests': self.request.GET.get('capacity') or self.hotel_room.capacity
        })

        return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['hotel_room'] = self.hotel_room
        return kwargs

    def form_valid(self, form):
        try:
            data = form.cleaned_data
            booking_service.create(
                user=self.request.user,
                check_in=data.get('check_in'),
                check_out=data.get('check_out'),
                number_of_guests=data.get('number_of_guests'),
                services=data.get('services', []),
                hotel_room=self.hotel_room,
            )

            return super().form_valid(form)
        except forms.ValidationError as error:
            form.add_error(None, error)
            return self.form_invalid(form)
        except BookingExistsException as error:
            form.add_error(None, error)
            return self.form_invalid(form)
