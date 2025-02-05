from django.urls import path
from .views import VehiculoListView, VehiculoCreateView, VehiculoUpdateView, VehiculoDeleteView

urlpatterns = [
    path('', VehiculoListView.as_view(), name='lista_vehiculos'),
    path('nuevo/', VehiculoCreateView.as_view(), name='crear_vehiculo'),
    path('editar/<int:pk>/', VehiculoUpdateView.as_view(), name='editar_vehiculo'),
    path('eliminar/<int:pk>/', VehiculoDeleteView.as_view(), name='eliminar_vehiculo'),
    path("buscar/<str:dominio>/", buscar_vehiculo, name="buscar_vehiculo"),
]
