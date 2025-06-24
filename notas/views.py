from django.shortcuts import render, redirect
from .models import NotaFiscal
from .forms import NotaFiscalForm
from django.contrib import messages

def lista_notas(request):
    notas = NotaFiscal.objects.all().order_by('-data_upload')
    return render(request, 'notas/lista_notas.html', {'notas': notas})

def cadastrar_nota(request):
    if request.method == 'POST':
        form = NotaFiscalForm(request.POST, request.FILES)
        if form.is_valid():
            nota = form.save()
            messages.success(request, "Nota fiscal cadastrada com sucesso!")
            # (aqui no futuro, pode adicionar: ler PDF, tentar OCR e preencher campos)
            return redirect('lista_notas')
        else:
            messages.error(request, "Erro ao cadastrar nota fiscal. Verifique os campos.")
    else:
        form = NotaFiscalForm()
    return render(request, 'notas/cadastrar_nota.html', {'form': form})
