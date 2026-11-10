import logging

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.user.forms.registration_form import RegistrationForm
from apps.user.services import user_service

logger = logging.getLogger(__name__)

class UserRegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        try:
            data = form.cleaned_data
            data['password'] = data.pop('password1')
            data.pop('password2')

            data['role'] = 'User'

            user_service.create(
                **data
            )

            return redirect(self.success_url)
        except ValueError as ex:
            form.add_error(None, str(ex))
            return self.form_invalid(form)
        except Exception as ex:
            logger.error(f"Unexpected error during user registration: {ex}")
            form.add_error(None, "An unexpected error occurred. Please try again later.")
            return self.form_invalid(form)
