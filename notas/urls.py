from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notas, name='lista_notas'),
    path('nova/', views.cadastrar_nota, name='cadastrar_nota'),
]
