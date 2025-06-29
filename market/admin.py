from django.contrib import admin
from .models import ItemMarket, Requisicao, ItemRequisitado

admin.site.register(ItemMarket)
admin.site.register(Requisicao)
admin.site.register(ItemRequisitado)
