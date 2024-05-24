from django import forms
from .models import Client

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
            'phone_number': forms.TextInput(attrs={'class': 'form-control form-control-half'}),
        }
