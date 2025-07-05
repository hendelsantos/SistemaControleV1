from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.gi_dashboard, name='gi_dashboard'),
    path('input-semana/', views.gi_input_semana, name='gi_input_semana'),
]