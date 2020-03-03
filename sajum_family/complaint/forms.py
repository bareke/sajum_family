from django import forms
from django.forms import ModelChoiceField

from .models import Officer
from .models import Vereda
from .models import Municipality

# Create your forms here


class OfficerForm(forms.ModelForm):
    vereda = ModelChoiceField(queryset=None)
    municipality = ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vereda'].queryset = Vereda.objects.all()
        self.fields['municipality'].queryset = Municipality.objects.all()
        self.fields['vereda'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'placeholder': 'Vereda',
        })
        self.fields['municipality'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'placeholder': 'Municipio',
        })

    class Meta:
        model = Officer
        fields = '__all__'
        labels = {
            'name_1': 'Primer nombre',
            'name_2': 'Segundo nombre',
            'lastname_1': 'Primer apellido',
            'lastname_2': 'Segundo apellido',
            'email': 'Correo',
            'profession': 'Profesión',
            'position': 'Posición',
            'vereda': 'Vereda',
            'municipality': 'Municipio'
        }
        widgets = {
            'name_1': forms.TextInput(attrs={
                'class': 'form-control form-control-sm'
            }),
            'name_2': forms.TextInput(attrs={
                'class': 'form-control form-control-sm'
            }),
            'lastname_1': forms.TextInput(attrs={
                'class': 'form-control form-control-sm'
            }),
            'lastname_2': forms.TextInput(attrs={
                'class': 'form-control form-control-sm'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control form-control-sm'
            }),
            'profession': forms.TextInput(attrs={
                'class': 'form-control form-control-sm'
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-control form-control-sm'
            }),
        }
