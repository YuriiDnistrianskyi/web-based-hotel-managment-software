from django import forms

from apps.booking.forms.fields import ServiceMultipleChoiceField
from apps.booking.models.booking import Booking
from apps.booking.services import service_service


class BookingCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            self.hotel_room = kwargs.pop('hotel_room')
    
            super().__init__(*args, **kwargs)
    
            self.__capacity = self.hotel_room.capacity
    
            self.fields['number_of_guests'].widget.attrs.update({
                'max': self.__capacity
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

            guests = cleaned_data.get('number_of_guests', 1)

            if guests < 1 or guests > self.__capacity:
                raise forms.ValidationError(
                    "Number of guests must be between 1 and capacity"  
                )

            return cleaned_data
