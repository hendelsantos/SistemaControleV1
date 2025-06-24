from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demandas.urls')),  # Redireciona / para o dashboard do app demandas
    path('notas/', include('notas.urls')),  # (quando criar urls.py no app notas)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
