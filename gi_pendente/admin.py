from django.contrib import admin
from .models import GiPendente

@admin.register(GiPendente)
class GiPendenteAdmin(admin.ModelAdmin):
    list_display = ['catalogo', 'material', 'quantidade', 'data', 'total']
    search_fields = ['catalogo', 'material', 'descricao']
    list_filter = ['data']
