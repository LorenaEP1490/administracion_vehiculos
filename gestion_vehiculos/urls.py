"""
URL configuration for gestion_vehiculos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("apps.autenticacion.urls")),  # Autenticación
    path("vehiculos/", include("apps.vehiculos.urls")),  # Vehículos
    path("inspecciones/", include("apps.inspecciones.urls")),  # Inspecciones
    path("gastos/", include("apps.gastos.urls")),  # Gastos
    path("publicaciones/", include("apps.publicaciones.urls")),  # Publicaciones
    path("transferencias/", include("apps.transferencias.urls")),  # Transferencias
]