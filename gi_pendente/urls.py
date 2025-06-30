from django.urls import path
from . import views

urlpatterns = [
    path('', views.gi_lista, name='gi_lista'),
    path('importar/', views.gi_importar_excel, name='gi_importar_excel'),
    # Remova ou comente a linha abaixo SE você ainda não criou a view:
    path('dashboard/', views.gi_dashboard, name='gi_dashboard'),
]
