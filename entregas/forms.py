from django import forms
from .models import Entrega


class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['morador', 'data_entrega', 'quantidade']