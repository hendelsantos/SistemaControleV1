# pm05/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.pm05_lista, name='pm05_lista'),  # <-- Corrigido aqui!
    path('novo/', views.novo_pm05, name='pm05_novo'),
    path('<int:pk>/', views.detalhe_pm05, name='pm05_detalhe'),
    # ... outros caminhos se quiser
]
