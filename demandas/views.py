from django.shortcuts import render, redirect
from .models import Demanda, Pedido
from .forms import DemandaForm

def dashboard(request):
    demandas_abertas = Demanda.objects.filter(etapa='aberto').count()
    demandas_cotacao = Demanda.objects.filter(etapa='cotado').count()
    demandas_finalizadas = Demanda.objects.filter(etapa='finalizado').count()
    return render(request, 'demandas/dashboard.html', {
        'demandas_abertas': demandas_abertas,
        'demandas_cotacao': demandas_cotacao,
        'demandas_finalizadas': demandas_finalizadas,
    })

def lista_demandas(request):
    demandas = Demanda.objects.all().order_by('-data_criacao')

    # --- Filtros Demandas ---
    id = request.GET.get('id')
    nome = request.GET.get('nome')
    descricao = request.GET.get('descricao')
    catalogo = request.GET.get('catalogo')
    quantidade = request.GET.get('quantidade')
    data = request.GET.get('data')
    etapa = request.GET.get('etapa')

    if id:
        demandas = demandas.filter(id=id)
    if nome:
        demandas = demandas.filter(nome__icontains=nome)
    if descricao:
        demandas = demandas.filter(descricao__icontains=descricao)
    if catalogo:
        demandas = demandas.filter(catalogo__icontains=catalogo)
    if quantidade:
        demandas = demandas.filter(quantidade=quantidade)
    if data:
        demandas = demandas.filter(data_criacao=data)
    if etapa:
        demandas = demandas.filter(etapa=etapa)

    context = {
        'demandas': demandas,
        'filtros': {
            'id': id or '',
            'nome': nome or '',
            'descricao': descricao or '',
            'catalogo': catalogo or '',
            'quantidade': quantidade or '',
            'data': data or '',
            'etapa': etapa or '',
        }
    }
    return render(request, 'demandas/lista_demandas.html', context)

def cadastrar_demanda(request):
    if request.method == 'POST':
        form = DemandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_demandas')
    else:
        form = DemandaForm()
    return render(request, 'demandas/nova_demanda.html', {'form': form})

def lista_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-data_criacao')

    # --- Filtros Pedidos ---
    id = request.GET.get('id')
    demanda = request.GET.get('demanda')
    valor = request.GET.get('valor')
    empresa = request.GET.get('empresa')
    previsao_entrega = request.GET.get('previsao_entrega')
    data_recebimento = request.GET.get('data_recebimento')
    data_pedido = request.GET.get('data_pedido')

    # CORRIGE: só aplica filtro se for número
    if id and id.isdigit():
        pedidos = pedidos.filter(id=int(id))
    if demanda:
        pedidos = pedidos.filter(demanda__nome__icontains=demanda)  # Ajuste conforme seu model
    if valor:
        pedidos = pedidos.filter(valor=valor)
    if empresa:
        pedidos = pedidos.filter(empresa__icontains=empresa)
    if previsao_entrega:
        pedidos = pedidos.filter(previsao_entrega=previsao_entrega)
    if data_recebimento:
        pedidos = pedidos.filter(data_recebimento=data_recebimento)
    if data_pedido:
        pedidos = pedidos.filter(data_criacao=data_pedido)

    context = {
        'pedidos': pedidos,
        'filtros': {
            'id': id or '',
            'demanda': demanda or '',
            'valor': valor or '',
            'empresa': empresa or '',
            'previsao_entrega': previsao_entrega or '',
            'data_recebimento': data_recebimento or '',
            'data_pedido': data_pedido or '',
        }
    }
    return render(request, 'demandas/lista_pedidos.html', context)
