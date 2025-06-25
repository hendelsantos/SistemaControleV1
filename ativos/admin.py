from django.contrib import admin
from .models import Ativo, FotoAtivo

class FotoAtivoInline(admin.TabularInline):
    model = FotoAtivo
    extra = 1

class AtivoAdmin(admin.ModelAdmin):
    list_display = ['numero_ativo', 'descricao', 'catalog', 'local_armazenamento', 'data_inventario']
    search_fields = ['numero_ativo', 'descricao', 'catalog', 'local_armazenamento']
    inlines = [FotoAtivoInline]

admin.site.register(Ativo, AtivoAdmin)
