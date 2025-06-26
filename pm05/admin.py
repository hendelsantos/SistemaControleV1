from django.contrib import admin
from .models import PM05Item, PM05Foto, PM05Arquivo

class FotoInline(admin.TabularInline):
    model = PM05Foto
    extra = 1

class ArquivoInline(admin.TabularInline):
    model = PM05Arquivo
    extra = 1

@admin.register(PM05Item)
class PM05ItemAdmin(admin.ModelAdmin):
    list_display = ('catalog_envio', 'descricao', 'fornecedor_enviado', 'data_envio')
    search_fields = ('catalog_envio', 'descricao', 'fornecedor_enviado')
    inlines = [FotoInline, ArquivoInline]
