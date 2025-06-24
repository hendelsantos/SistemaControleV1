from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('demandas/', views.lista_demandas, name='lista_demandas'),
    path('demandas/nova/', views.cadastrar_demanda, name='cadastrar_demanda'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
]
