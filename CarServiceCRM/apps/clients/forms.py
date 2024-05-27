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

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        middle_name = cleaned_data.get('middle_name')
        phone_number = cleaned_data.get('phone_number')

        # Исключаем текущую запись из проверки уникальности
        if self.instance.pk:
            if Client.objects.filter(first_name=first_name, last_name=last_name, middle_name=middle_name, phone_number=phone_number).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Клиент с таким именем, фамилией, отчеством и номером телефона уже существует.")
        else:
            if Client.objects.filter(first_name=first_name, last_name=last_name, middle_name=middle_name, phone_number=phone_number).exists():
                raise forms.ValidationError("Клиент с таким именем, фамилией, отчеством и номером телефона уже существует.")

        return cleaned_data
