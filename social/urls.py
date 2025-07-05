from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='social_feed'),
    path('postar/', views.novo_post, name='novo_post'),
    path('comentar/<int:post_id>/', views.novo_comentario, name='novo_comentario'),
]