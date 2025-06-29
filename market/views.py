from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from demandas.models import Demanda
from .models import ItemMarket

def market_dashboard(request):
    filtro = request.GET.get('q', '')
    itens = ItemMarket.objects.all()
    if filtro:
        itens = itens.filter(
            nome__icontains=filtro
        )
    # Adicionando paginação
    paginator = Paginator(itens, 12)  # 12 itens por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'market/market_dashboard.html',
        {
            'itens': page_obj,  # agora 'itens' é o objeto de página
            'filtro': filtro,
            'page_obj': page_obj,  # envia também, caso queira usar diretamente
        }
    )

def market_requisitar(request, item_id):
    item = get_object_or_404(ItemMarket, id=item_id)
    if request.method == "POST":
        nome = request.POST.get('solicitante')
        quantidade = int(request.POST.get('quantidade', 1))
        # Cria a demanda automaticamente
        Demanda.objects.create(
            nome=nome,
            descricao=item.descricao,
            catalogo=item.catalogo,
            quantidade=quantidade,
        )
        return redirect('lista_demandas')  # ajuste para o nome correto da sua URL de demandas
    return render(request, 'market/market_requisitar.html', {'item': item})
