from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ativos, name='lista_ativos'),
    path('novo/', views.cadastrar_ativo, name='cadastrar_ativo'),
    path('<int:pk>/', views.detalhe_ativo, name='detalhe_ativo'),
    path('<int:pk>/editar/', views.editar_ativo, name='editar_ativo'),
    path('<int:pk>/excluir/', views.excluir_ativo, name='excluir_ativo'),
    path('<int:pk>/adicionar-foto/', views.adicionar_foto, name='adicionar_foto'),
]
