import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(
        max_length=15, 
            validators=[RegexValidator(
            regex=r'^\+[1-9]\d{7,14}$',
            message='Enter a valid phone number.'
        )])
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise forms.ValidationError("Passwords do not match")
        if cleaned_data.get("date_of_birth") and cleaned_data.get('date_of_birth') > datetime.date.today():
            raise forms.ValidationError("Date of birth cannot be in the future")

        return cleaned_data
