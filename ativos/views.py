from django.shortcuts import render, redirect, get_object_or_404
from .models import Ativo, FotoAtivo
from .forms import AtivoForm, FotoAtivoForm
from django.core.paginator import Paginator

def lista_ativos(request):
    filtro = request.GET.get('q')
    ativos = Ativo.objects.all()
    if filtro:
        ativos = ativos.filter(descricao__icontains=filtro)
    paginator = Paginator(ativos, 10)  # 10 por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ativos/lista_ativos.html', {'page_obj': page_obj})

def cadastrar_ativo(request):
    if request.method == 'POST':
        form = AtivoForm(request.POST, request.FILES)
        if form.is_valid():
            ativo = form.save()
            return redirect('detalhe_ativo', pk=ativo.pk)
    else:
        form = AtivoForm()
    return render(request, 'ativos/cadastrar_ativo.html', {'form': form})

def detalhe_ativo(request, pk):
    ativo = get_object_or_404(Ativo, pk=pk)
    fotos = FotoAtivo.objects.filter(ativo=ativo)
    foto_form = FotoAtivoForm()
    return render(request, 'ativos/detalhe_ativo.html', {'ativo': ativo, 'fotos': fotos, 'foto_form': foto_form})

def editar_ativo(request, pk):
    ativo = get_object_or_404(Ativo, pk=pk)
    if request.method == 'POST':
        form = AtivoForm(request.POST, request.FILES, instance=ativo)
        if form.is_valid():
            form.save()
            return redirect('detalhe_ativo', pk=ativo.pk)
    else:
        form = AtivoForm(instance=ativo)
    return render(request, 'ativos/editar_ativo.html', {'form': form, 'ativo': ativo})

def excluir_ativo(request, pk):
    ativo = get_object_or_404(Ativo, pk=pk)
    if request.method == 'POST':
        ativo.delete()
        return redirect('lista_ativos')
    return render(request, 'ativos/deletar_ativo.html', {'ativo': ativo})

def adicionar_foto(request, pk):
    ativo = get_object_or_404(Ativo, pk=pk)
    if request.method == 'POST':
        form = FotoAtivoForm(request.POST, request.FILES)
        if form.is_valid():
            foto = form.save(commit=False)
            foto.ativo = ativo
            foto.save()
            return redirect('detalhe_ativo', pk=pk)
    else:
        form = FotoAtivoForm()
    return render(request, 'ativos/adicionar_foto.html', {'form': form, 'ativo': ativo})
