from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.urls import reverse
from main.models import MenuPrincipal, CustomUser
import shutil
import os
import json

# Create your views here.

def contexto_base(request):
    query_set = MenuPrincipal.objects.all()
    itens_menu = list(query_set.values())
    context = { 'itens_menu': itens_menu }
    
    if request.user.is_authenticated:
        usuario = request.user
        context['usuario'] = {
            'username': usuario.username,
            'nome': usuario.nome,
            'perfil': usuario.perfil,
        }
    
    return context

def index(request):
    return render(request, 'index.html')

def viewLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificar se login ou password estão em branco
        if not username or not password:
            messages.error(request, 'Por favor, forneça usuário e senha.')
            return render(request, 'viewLogin.html')

        # Autenticar o usuário
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Usuário autenticado com sucesso
            django_login(request, user)
            return redirect('home')  # redirecionar para a página inicial após o login
        else:
            # Falha na autenticação
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'viewLogin.html')

def criarUsuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Usuário criado com sucesso. Faça o login.')
            return redirect('viewLogin')  # Redireciona para a página de login
        else:
            # Adicione a mensagem de erro ao contexto
            messages.error(request, 'Erro ao criar usuário. Por favor, verifique o preenchimento correto dos campos.')
    else:
        # Use o novo formulário ao renderizar a página inicial
        form = CustomUserCreationForm()

    # Inclua o contexto com o formulário e as mensagens de erro
    context = {'form': form}
    return render(request, 'criarUsuario.html', context)


def home(request):
    """Funcao view para HomePage."""
    context = contexto_base(request)
    if request.method == "POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        upload = fs.url(filename)
        context['uploaded'] = upload
        
    return render(request, 'home.html', context)

def contato(request):
    context = contexto_base(request)
    return render(request, 'contato.html', context)

def ajuda(request):
    context = contexto_base(request)
    return render(request, 'ajuda.html', context)

def sobre(request):
    context = contexto_base(request)
    return render(request, 'sobre.html', context)
    
def video(request):
    with open('IA/events.json') as time_stamps_json:
        time_stamps_file = json.load(time_stamps_json)
    
    fps = 30
    video_length = 18
    context = contexto_base(request)
    fs = FileSystemStorage()
    dict = fs.listdir(fs.location)
    file = fs.url(dict[1][0])

    context["file"] = file
    context["time_stamps_file"] = time_stamps_file
    context["fps"] = fps
    context["video_length"] = video_length
    return render(request, 'video.html', context)