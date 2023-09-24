from django.urls import path
from main.views import index, home, contato, ajuda, sobre, video
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('contato/', contato, name='contato'),
    path('ajuda/', ajuda, name='ajuda'),
    path('sobre/', sobre, name='sobre'),
    path('video/', video, name='video'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)