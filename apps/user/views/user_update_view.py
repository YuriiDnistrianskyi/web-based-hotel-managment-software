from django import forms
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.user.forms.user_update_form import UserUpdateForm
from apps.user.mixins import UserRequiredMixin
from apps.user.models.user import User
from apps.user.services import user_service


class UserUpdateView(UserRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/edit.html'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        try:
            user_service.update(
                obj_id=self.request.user.id,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
    
            return redirect(reverse_lazy('account'))
        except forms.ValidationError as error:
            form.add_error(None, error)
            return self.form_invalid(form)
