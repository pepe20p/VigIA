from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.hmtl')

def faq(request):
    return render(request, 'faq.hmtl')
