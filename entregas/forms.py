from django import forms
from .models import Entrega


class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['morador', 'data_entrega', 'quantidade']

        widgets = {
            'morador': forms.Select(attrs={'class': 'form-control', 'id': 'id_morador'}),
            'data_entrega': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }