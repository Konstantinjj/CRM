from django import forms
from .models import Client
import re

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'middle_name', 'phone_number']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество',
            'phone_number': 'Номер телефона'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-half'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-half'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control form-control-half'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control form-control-half', 'placeholder': '+7(XXX)-XXX-XX-XX'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        pattern = re.compile(r'^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$')
        if not pattern.match(phone_number):
            raise forms.ValidationError("Номер телефона должен быть в формате +7(XXX)-XXX-XX-XX")
        return phone_number
