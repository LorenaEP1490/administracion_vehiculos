from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  # 🔹 Para mostrar mensajes de error en el login

def login_view(request):
    """ Vista para iniciar sesión en el sistema. """
    if request.user.is_authenticated:
        return redirect("inicio")  # Si el usuario ya está autenticado, redirigir a la página de inicio.

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)

            # 📌 Redirigir al usuario a la página que intentó acceder antes de hacer login
            next_url = request.GET.get("next", "inicio")
            return redirect(next_url)
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")  # 🔹 Mensaje de error si falla la autenticación

    else:
        form = AuthenticationForm()

    return render(request, "autenticacion/login.html", {"form": form})


@login_required(login_url="login")  # 🔹 Asegura que solo usuarios autenticados accedan a 'inicio'
def inicio(request):
    """ Vista de la página principal después de iniciar sesión. """
    return render(request, "inicio.html")


def logout_view(request):
    """ Cerrar sesión y redirigir al login. """
    logout(request)
    messages.success(request, "Sesión cerrada correctamente.")  # 🔹 Mensaje de confirmación de logout
    return redirect("login")  # Redirigir al login después de cerrar sesión
