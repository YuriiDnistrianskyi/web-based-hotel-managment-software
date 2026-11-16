from django import forms

from apps.booking.forms.fields import ServiceMultipleChoiceField
from apps.booking.models.booking import Booking
from apps.booking.services import service_service


class BookingUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk and not self.is_bound:
            self.fields['services'].initial = self.instance.services.all()

            capacity = self.instance.hotel_room.capacity

            self.fields['number_of_guests'].widget.attrs.update({
                'max': capacity
            })

    services = ServiceMultipleChoiceField(
        queryset=service_service.get(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Booking
        fields = [
            'check_in',
            'check_out',
            'number_of_guests'
        ]
        widgets = {
            'check_in': forms.DateInput(attrs={
                'type': 'date',
            }),
            'check_out': forms.DateInput(attrs={
                'type': 'date',
            }),
            'number_of_guests': forms.NumberInput(attrs={
                'type': 'number',
                'min': 1
            })
        }

    def clean(self):
        cleaned_data = super().clean()

        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_in and check_out and check_in >= check_out:
            raise forms.ValidationError(
                "Check-out date must be after check-in date."
            )

        guests = int(cleaned_data.get('number_of_guests'))
        capacity = self.instance.hotel_room.capacity

        if guests < 1 or guests > capacity:
            raise forms.ValidationError(
                "Number of guests must be between 1 and capacity"  
            )

        return cleaned_data
