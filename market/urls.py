from django.urls import path
from . import views

urlpatterns = [
    path('', views.market_dashboard, name='market_dashboard'),
    path('dashboard/', views.market_dashboard, name='market_dashboard'),
    path('requisitar/<int:item_id>/', views.market_requisitar, name='market_requisitar'),
]
