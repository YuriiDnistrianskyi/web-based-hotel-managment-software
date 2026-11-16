from django import forms

from apps.booking.models.booking import Booking

class BookingUpdateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'check_in',
            'check_out',
            'spa',
            'meals',
            'transfer',
        ]
        widgets = {
            'check_in': forms.DateInput(attrs={
                'type': 'date',
            }),
            'check_out': forms.DateInput(attrs={
                'type': 'date',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_in and check_out and check_in >= check_out:
            raise forms.ValidationError(
                "Check-out date must be after check-in date."
            )

        return cleaned_data
