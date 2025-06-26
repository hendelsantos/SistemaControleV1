from django.shortcuts import render, get_object_or_404, redirect
from .models import PM05Item, PM05Foto, PM05Arquivo
from .forms import PM05ItemForm, PM05FotoForm, PM05ArquivoForm
from django.core.paginator import Paginator

def pm05_lista(request):
    filtro = request.GET.get('q', '')
    # Ordena do mais novo para o mais velho pela data_envio
    itens = PM05Item.objects.all().order_by('-data_envio')
    if filtro:
        itens = itens.filter(descricao__icontains=filtro)
    paginator = Paginator(itens, 8)  # Exibe 8 cards por página (2 linhas de 2)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'pm05/lista_pm05.html', {'page_obj': page_obj, 'filtro': filtro})

def novo_pm05(request):
    if request.method == 'POST':
        form = PM05ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('pm05_detalhe', pk=item.pk)

    else:
        form = PM05ItemForm()
    return render(request, 'pm05/novo_pm05.html', {'form': form})

def detalhe_pm05(request, pk):
    item = get_object_or_404(PM05Item, pk=pk)
    fotos = item.fotos.all()
    arquivos = item.arquivos.all()
    return render(request, 'pm05/detalhe_pm05.html', {'item': item, 'fotos': fotos, 'arquivos': arquivos})
