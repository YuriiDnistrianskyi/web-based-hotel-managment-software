from django import forms

from apps.user.models.user import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput()
        }
