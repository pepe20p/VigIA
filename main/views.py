from django.shortcuts import render

# Create your views here.
from django.core.files.storage import FileSystemStorage
import shutil
from django.conf import settings
from main.models import MenuPrincipal
import os
import json

def contexto_menu():
    query_set = MenuPrincipal.objects.all()
    itens_menu = list(query_set.values())
    context = { 'itens_menu': itens_menu }
    return context

def index(request):
    return render(request, 'index.html')

def home(request):
    """Funcao view para HomePage."""
    context = contexto_menu()
    if request.method == "POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        upload = fs.url(filename)
        context['uploaded'] = upload
        
    return render(request, 'home.html', context)

def contato(request):
    context = contexto_menu()
    return render(request, 'contato.html', context)

def ajuda(request):
    context = contexto_menu()
    return render(request, 'ajuda.html', context)

def sobre(request):
    context = contexto_menu()
    return render(request, 'sobre.html', context)
    
def video(request):
    with open('IA/events.json') as time_stamps_json:
        time_stamps_file = json.load(time_stamps_json)
    
    fps = 30
    video_length = 18
    context = contexto_menu()
    fs = FileSystemStorage()
    dict = fs.listdir(fs.location)
    file = fs.url(dict[1][0])

    context["file"] = file
    context["time_stamps_file"] = time_stamps_file
    context["fps"] = fps
    context["video_length"] = video_length
    return render(request, 'video.html', context)