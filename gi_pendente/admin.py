from django.contrib import admin
from .models import GiPendenteSemana

@admin.register(GiPendenteSemana)
class GiPendenteSemanaAdmin(admin.ModelAdmin):
    list_display = ['semana', 'gi_realizado', 'gi_devido']
    search_fields = ['semana']
    list_filter = ['semana']