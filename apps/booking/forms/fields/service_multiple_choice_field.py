from django import forms
from django.utils.html import format_html


class ServiceMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return format_html(
            '<div>'
                '<strong style="font-size: 18px;">{}</strong>'
                '<p style="font-size: 13px; font-weight: normal; color: #777;">{}</p>'
                '<span style="font-size: 16px; font-weight: bold;">Price: {} ₴</span>'
            '</div>',
            obj.title,
            obj.description,
            obj.price
        )
