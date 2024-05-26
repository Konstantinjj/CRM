from django import forms
from .models import WorkType

class WorkTypeForm(forms.ModelForm):
    class Meta:
        model = WorkType
        fields = ['name', 'cost']
        labels = {
            'name': 'Наименование работы',
            'cost': 'Стоимость'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-half'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control form-control-half'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if self.instance.pk:
            if WorkType.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Работа с таким наименованием уже существует.")
        else:
            if WorkType.objects.filter(name=name).exists():
                raise forms.ValidationError("Работа с таким наименованием уже существует.")

        return name
