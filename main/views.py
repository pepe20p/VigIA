from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import shutil 
# Create your views here.
def index(request):
    if request.method == "POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        upload = fs.url(filename)
        return render(
            request,
            'index.html',
            {'uploaded': upload},
        )
        
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def ajuda(request):
    return render(request, 'ajuda.html')

def sobre(request):
    return render(request, 'sobre.html')