from django import forms
from .models import Ativo, FotoAtivo

class AtivoForm(forms.ModelForm):
    class Meta:
        model = Ativo
        fields = '__all__'

class FotoAtivoForm(forms.ModelForm):
    class Meta:
        model = FotoAtivo
        fields = ['imagem', 'descricao']
