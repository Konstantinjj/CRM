from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['gos_num', 'vin_number', 'brand', 'model', 'year_of_production', 'client']
        labels = {
            'gos_num': 'Гос номер',
            'vin_number': 'ВИН номер',
            'brand': 'Марка',
            'model': 'Модель',
            'year_of_production': 'Год выпуска',
            'client': 'Клиент'
        }
        widgets = {
            'gos_num': forms.TextInput(attrs={'class': 'form-control form-control-half'}),
            'vin_number': forms.TextInput(attrs={'class': 'form-control form-control-half'}),
            'brand': forms.TextInput(attrs={'class': 'form-control form-control-half'}),
            'model': forms.TextInput(attrs={'class': 'form-control form-control-half'}),
            'year_of_production': forms.NumberInput(attrs={'class': 'form-control form-control-half'}),
            'client': forms.Select(attrs={'class': 'form-control form-control-half'}),
        }
