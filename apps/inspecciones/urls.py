from django.urls import path
from .views import (
    InspeccionListView,
    InspeccionAccesoriosCreateView, InspeccionAccesoriosUpdateView, InspeccionAccesoriosDeleteView
)

urlpatterns = [
    path('<str:dominio>/', InspeccionListView.as_view(), name='lista_inspecciones'),
    
    # URLs para Inspección de Accesorios
    path('accesorios/nueva/', InspeccionAccesoriosCreateView.as_view(), name='crear_inspeccion_accesorios'),
    path('accesorios/editar/<int:pk>/', InspeccionAccesoriosUpdateView.as_view(), name='editar_inspeccion_accesorios'),
    path('accesorios/eliminar/<int:pk>/', InspeccionAccesoriosDeleteView.as_view(), name='eliminar_inspeccion_accesorios'),
]
