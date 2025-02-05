from django.contrib import admin
from django.urls import path, include  # <-- Asegúrate de que 'include' está importado
from .views import inicio  # Importar la vista de inicio

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("apps.autenticacion.urls")),  # Autenticación
    path("vehiculos/", include("apps.vehiculos.urls")),  # Vehículos
    path("inspecciones/", include("apps.inspecciones.urls")),  # Inspecciones
    path("gastos/", include("apps.gastos.urls")),  # Gastos
    path("publicaciones/", include("apps.publicaciones.urls")),  # Publicaciones
    path("transferencias/", include("apps.transferencias.urls")),  # Transferencias
    path("", inicio, name="inicio"),  # Página de inicio
]