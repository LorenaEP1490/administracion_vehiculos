from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import RegistroForm, LoginForm

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("dashboard")  # Redirigir al panel principal
    else:
        form = RegistroForm()
    return render(request, "autenticacion/registro.html", {"form": form})

def iniciar_sesion(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("dashboard")
    else:
        form = LoginForm()
    return render(request, "autenticacion/login.html", {"form": form})

def cerrar_sesion(request):
    logout(request)
    return redirect("login")
