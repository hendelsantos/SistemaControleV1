from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demandas.urls')),         # Raiz do site leva para demandas
    path('notas/', include('notas.urls')),      # App de notas fiscais
    path('ativos/', include('ativos.urls')),    # App de ativos (controle de ativos)
    path('pm05/', include('pm05.urls')),        # App PM05 (controle de envio de itens)
]

# Servir arquivos de mídia em modo DEBUG (fotos dos ativos, uploads etc.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
