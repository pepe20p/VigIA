from django.urls import path
from main.views import index, contato, faq

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('faq/', faq, name='faq'),
    
]