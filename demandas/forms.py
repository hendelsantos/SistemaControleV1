from django import forms
from .models import Demanda

class DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['nome', 'descricao', 'catalogo', 'quantidade']
