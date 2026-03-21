from django import forms
from .models import Morador

class MoradorForm(forms.ModelForm):
    class Meta:
        model = Morador
        fields = ['nome', 'cpf', 'telefone', 'endereco', 'ativo']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }