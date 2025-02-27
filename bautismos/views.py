from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from . models import Pais
from . forms import BautismoForm
from . forms import PaisForm


def menu_principal(request):
    return render(request, 'menuPartidas.html')

def user_login(request):
    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("menu_principal")  # Redirige a la vista del menú principal
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, "login.html", {"form": form})



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
            return render(request, 'succesBautismo.html', {'form': form})  # Redirigir a una lista de bautismos
    else:
        form = BautismoForm()

    return render(request, 'BautismoPartidas.html', {'form': form})