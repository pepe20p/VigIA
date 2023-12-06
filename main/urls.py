from django.urls import path
from main.views import index, home, contato, ajuda, sobre, video, viewLogin, criarUsuario
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('contato/', contato, name='contato'),
    path('ajuda/', ajuda, name='ajuda'),
    path('sobre/', sobre, name='sobre'),
    path('video/', video, name='video'),
    path('viewLogin/', viewLogin, name='viewLogin'),
    path('criarUsuario/', criarUsuario, name='criarUsuario'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)