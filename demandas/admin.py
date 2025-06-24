from django.contrib import admin
from .models import Demanda, Pedido

@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'catalogo', 'quantidade', 'data_criacao', 'etapa')
    search_fields = ('nome', 'descricao', 'catalogo')
    list_filter = ('etapa', 'data_criacao')
    ordering = ('-data_criacao',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'demanda', 'valor', 'empresa', 'previsao_entrega', 'data_recebimento')
    search_fields = ('empresa', 'demanda__nome')
    list_filter = ('empresa', 'previsao_entrega')
    ordering = ('-previsao_entrega',)
