from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['gos_num', 'vin_number', 'brand', 'model', 'year_of_production', 'client']
