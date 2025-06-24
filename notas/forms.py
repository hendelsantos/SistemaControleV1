from django import forms
from .models import NotaFiscal

class NotaFiscalForm(forms.ModelForm):
    class Meta:
        model = NotaFiscal
        fields = [
            'numero',
            'empresa',
            'data_emissao',
            'valor',
            'mes_entrada',
            'arquivo'
        ]
        widgets = {
            'data_emissao': forms.DateInput(attrs={'type': 'date'}),
            'mes_entrada': forms.TextInput(attrs={'placeholder': 'MM/YYYY'}),
        }
