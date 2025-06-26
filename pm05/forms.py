from django import forms
from .models import PM05Item, PM05Foto, PM05Arquivo

class PM05ItemForm(forms.ModelForm):
    class Meta:
        model = PM05Item
        fields = '__all__'

class PM05FotoForm(forms.ModelForm):
    class Meta:
        model = PM05Foto
        fields = ['imagem', 'descricao']

class PM05ArquivoForm(forms.ModelForm):
    class Meta:
        model = PM05Arquivo
        fields = ['arquivo', 'descricao']
