from django.urls import path
from main.views import index, contato, ajuda, sobre

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('ajuda/', ajuda, name='ajuda'),
    path('sobre/', sobre, name='sobre'),
]