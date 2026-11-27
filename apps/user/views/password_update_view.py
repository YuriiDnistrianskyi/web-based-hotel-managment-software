import logging

from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.user.exceptions import InvalidPasswordException
from apps.user.forms.password_update_from import PasswordUpdateForm
from apps.user.mixins import UserRequiredMixin
from apps.user.services import auth_service

logger = logging.getLogger(__name__)

class PasswordUpdateView(UserRequiredMixin, FormView):
    form_class = PasswordUpdateForm
    template_name = 'user/password_edit.html'
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        try:
            data = form.cleaned_data

            auth_service.change_password(
                user=self.request.user,
                old_password=data.get('old_password'),
                new_password=data.get('new_password_1')
            )

            update_session_auth_hash(self.request, self.request.user)
            
            return super().form_valid(form)

        except InvalidPasswordException as ex:
            form.add_error(None, ex)
            return self.form_invalid(form)
        except Exception:
            logger.exception("Unexpected error during user registration")
            form.add_error(None, "An unexpected error occurred. Please try again later.")
            return self.form_invalid(form)
