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

    def clean_gos_num(self):
        gos_num = self.cleaned_data.get('gos_num')

        # Исключаем текущую запись из проверки уникальности
        if self.instance.pk:
            if Car.objects.filter(gos_num=gos_num).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Машина с таким государственным номером уже существует.")
        else:
            if Car.objects.filter(gos_num=gos_num).exists():
                raise forms.ValidationError("Машина с таким государственным номером уже существует.")

        return gos_num
