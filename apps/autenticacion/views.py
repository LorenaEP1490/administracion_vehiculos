from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect("inicio")  # Si ya está autenticado, redirigir a la página principal

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("inicio")  # Redirigir al usuario después de iniciar sesión
    else:
        form = AuthenticationForm()

    return render(request, "autenticacion/login.html", {"form": form})

@login_required  # 🚀 Protege la página de inicio: solo usuarios autenticados pueden acceder
def inicio(request):
    return render(request, "inicio.html")

def logout_view(request):
    logout(request)
    return redirect("login")  # Redirige al login después de cerrar sesión
