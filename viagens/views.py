from django.shortcuts import render
from django.urls import is_valid_path
from viagens.forms import ViagemForms

# Create your views here.

def index(request):
    form = ViagemForms()
    contexto = {'form' : form}
    return render(request, 'index.html', contexto)


def revConsulta(request):
    if request.method == 'POST':
        form = ViagemForms(request.POST)
        if form.is_valid():
            contexto = {'form' : form}
            return render(request, 'consulta.html', contexto)
        else:
            print('Formulário inválido!')   
            contexto = {'form' : form}
            return render(request, 'index.html', contexto)
