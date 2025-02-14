from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from . models import Pais
from . forms import BautismoForm
from . forms import PaisForm
from .forms import UserLogin

def menu_principal(request):
    return render(request, 'menuPartidas.html')

def login(request):
    return render(request, 'login.html')



def paisform(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()          
        return render(request, 'success.html', {'form': form}) 
    else:
        form = PaisForm()
    return render(request, 'paisform.html', {'form': form})


def lista_paises(request):
    paises = Pais.objects.all()
    return render(request, 'lista_paises.html', {'paises': paises})

def editar_pais(request, pk):
    pais = get_object_or_404(Pais, pk=pk)
    if request.method == 'POST':
        form = PaisForm(request.POST, instance=pais)
        if form.is_valid():
            form.save()
            return redirect('lista_paises')
    else:
        form = PaisForm(instance=pais)
    return render(request, 'editar_pais.html', {'form': form, 'pais': pais})


def eliminar_pais(request, pk):
    pais = get_object_or_404(Pais, pk=pk)
    if request.method == 'POST':
        pais.delete()
        return redirect('lista_paises')
    return render(request, 'eliminar_pais.html', {'pais': pais})



def bautismopartida(request):
    if request.method == 'POST':
        form = BautismoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success.html')  # Redirigir a una lista de bautismos
    else:
        form = BautismoForm()

    return render(request, 'BautismoPartidas.html', {'form': form})