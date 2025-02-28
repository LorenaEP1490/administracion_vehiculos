from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.autenticacion.views import inicio
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Rutas de autenticación
    path("auth/", include("apps.autenticacion.urls")),
    path("auth/login/", auth_views.LoginView.as_view(template_name="autenticacion/login.html"), name="login"),
    path("auth/logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    # Rutas de cada módulo
    path("vehiculos/", include("apps.vehiculos.urls")),
    path("inspecciones/", include("apps.inspecciones.urls")),
    path("gastos/", include("apps.gastos.urls")),
    path("publicaciones/", include("apps.publicaciones.urls")),
    path("transferencias/", include("apps.transferencias.urls")),

    # Proteger la página de inicio con login_required
    path("", login_required(inicio, login_url="login"), name="inicio"),
]
