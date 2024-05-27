from django import forms
from .models import Item, SortGroup

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'cost', 'quantity', 'sort_group']
        labels = {
            'name': 'Наименование позиции',
            'cost': 'Стоимость',
            'quantity': 'Количество',
            'sort_group': 'Группа сортировки'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-half'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control form-control-half'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control form-control-half'}),
            'sort_group': forms.Select(attrs={'class': 'form-control form-control-half'}),
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

class SortGroupForm(forms.ModelForm):
    class Meta:
        model = SortGroup
        fields = ['name']
        labels = {
            'name': 'Наименование группы'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-half'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if self.instance.pk:
            if SortGroup.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Группа с таким наименованием уже существует.")
        else:
            if SortGroup.objects.filter(name=name).exists():
                raise forms.ValidationError("Группа с таким наименованием уже существует.")
        return name
