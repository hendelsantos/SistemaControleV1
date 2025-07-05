from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demandas/', include('demandas.urls')),      # Agora demandas acessível em /demandas/
    path('notas/', include('notas.urls')),
    path('ativos/', include('ativos.urls')),
    path('pm05/', include('pm05.urls')),
    path('market/', include('market.urls')),
    path('gi/', include('gi_pendente.urls')),
    path('', include('social.urls')),                 # Social é a home e o menu Social
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)