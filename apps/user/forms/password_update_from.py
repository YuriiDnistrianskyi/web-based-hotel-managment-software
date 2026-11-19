from django import forms


class PasswordUpdateForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput
    )
    new_password_1 = forms.CharField(
        widget=forms.PasswordInput
    )
    new_password_2 = forms.CharField(
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('new_password_1') != cleaned_data.get('new_password_2'):
            raise forms.ValidationError('Passwords do not match')
        
        return cleaned_data 
