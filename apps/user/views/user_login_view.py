import logging

from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.user.forms.login_form import LoginForm
from apps.user.services import auth_service

logger = logging.getLogger(__name__)

class UserLoginView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        try:
            user = auth_service.authenticate(
                self.request,
                form.cleaned_data['email'],
                form.cleaned_data['password']
            )

            if user is None:
                form.add_error(None, 'Invalid email or password')
                return self.form_invalid(form)

            auth_service.login(self.request, user)

            return super().form_valid(form)
        except Exception as ex:
            logger.error(f"Unexpected error during user registration: {ex}")
            form.add_error(None, "An unexpected error occurred. Please try again later.")
            return self.form_invalid(form)
