from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'cost', 'quantity']
        labels = {
            'name': 'Наименование позиции',
            'cost': 'Стоимость',
            'quantity': 'Количество'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-half'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control form-control-half', 'step': '0.01'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control form-control-half', 'step': '0.01'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if self.instance.pk:
            if Item.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Позиция с таким наименованием уже существует.")
        else:
            if Item.objects.filter(name=name).exists():
                raise forms.ValidationError("Позиция с таким наименованием уже существует.")

        return name