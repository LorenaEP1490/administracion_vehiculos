from django.urls import path
from .views import lista_vehiculos, crear_vehiculo, editar_vehiculo, eliminar_vehiculo, buscar_vehiculo

urlpatterns = [
    path("", lista_vehiculos, name="lista_vehiculos"),
    path("crear/", crear_vehiculo, name="crear_vehiculo"),
    path("editar/<int:pk>/", editar_vehiculo, name="editar_vehiculo"),
    path("eliminar/<int:pk>/", eliminar_vehiculo, name="eliminar_vehiculo"),
    path("buscar/<str:dominio>/", buscar_vehiculo, name="buscar_vehiculo"),
]
