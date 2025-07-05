from django import forms
from .models import GiPendenteSemana

class GiPendenteSemanaForm(forms.ModelForm):
    class Meta:
        model = GiPendenteSemana
        fields = ['semana', 'gi_realizado', 'gi_devido']
        labels = {
            'semana': 'Semana (nº)',
            'gi_realizado': 'GI Realizado (R$)',
            'gi_devido': 'GI Devido (R$)',
        }
        widgets = {
            'semana': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 23'}),
            'gi_realizado': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Ex: 1500.00'}),
            'gi_devido': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Ex: 2000.00'}),
        }