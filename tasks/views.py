from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Equipo
from .forms import EquipoForm

# Vistas de Autenticación
def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        if request.POST["password"] == request.POST["confirmation_password"]:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                user.save()
                login(request, user)
                return redirect("lista_equipos")
            except IntegrityError:
                return render(request, "signup.html", {"form": UserCreationForm(), "error": "Error al crear el usuario"})
        else:
            return render(request, "signup.html", {"form": UserCreationForm(), "error": "Error, Las contraseñas no coinciden"})

def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, "signin.html", {"form": AuthenticationForm(), "error": "Usuario o contraseña incorrecta"})
        else:
            login(request, user)
            return redirect("lista_equipos")


def signout(request):
    logout(request)
    return redirect("home")

# Vistas para Equipos de Fútbol

def lista_equipos(request):
    equipos = Equipo.objects.filter(usuario=request.user)
    return render(request, "lista_equipos.html", {'equipos': equipos})


def crear_equipo(request):
    if request.method == 'GET':
        return render(request, 'crear_equipo.html', {'form': EquipoForm()})
    else:
        equipo = Equipo.objects.create(
            nombre = request.POST['nombre'],
            pais = request.POST['pais'],
            entrenador = request.POST['entrenador'],
            usuario = request.user
        )
        return redirect('lista_equipos')


def detalle_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id, usuario=request.user)
    if request.method == 'GET':
        form = EquipoForm(instance=equipo)
        return render(request, 'detalle_equipo.html', {'equipo': equipo, 'form': form})
    else:
        form = EquipoForm(request.POST, instance=equipo)
        form.save()
        return redirect('lista_equipos')


def eliminar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id, usuario=request.user)
    equipo.delete()
    return redirect('lista_equipos')