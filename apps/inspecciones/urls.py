from django.urls import path
from .views import (
    InspeccionListView,
    InspeccionAccesoriosCreateView, InspeccionAccesoriosUpdateView, InspeccionAccesoriosDeleteView,
    InspeccionMecanicaCreateView, InspeccionMecanicaUpdateView, InspeccionMecanicaDeleteView,
    InspeccionExteriorCreateView, InspeccionExteriorUpdateView, InspeccionExteriorDeleteView,
    InspeccionInteriorCreateView, InspeccionInteriorUpdateView, InspeccionInteriorDeleteView
)

urlpatterns = [
    # 🔎 Vista principal de inspecciones de un vehículo por dominio
    path('<str:dominio>/', InspeccionListView.as_view(), name='lista_inspecciones'),

    # 🔧 Inspección de Accesorios
    path('<str:dominio>/accesorios/nueva/', InspeccionAccesoriosCreateView.as_view(), name='crear_inspeccion_accesorios'),
    path('<str:dominio>/accesorios/editar/<int:pk>/', InspeccionAccesoriosUpdateView.as_view(), name='editar_inspeccion_accesorios'),
    path('<str:dominio>/accesorios/eliminar/<int:pk>/', InspeccionAccesoriosDeleteView.as_view(), name='eliminar_inspeccion_accesorios'),

    # 🔧 Inspección Mecánica
    path('<str:dominio>/mecanica/nueva/', InspeccionMecanicaCreateView.as_view(), name='crear_inspeccion_mecanica'),
    path('<str:dominio>/mecanica/editar/<int:pk>/', InspeccionMecanicaUpdateView.as_view(), name='editar_inspeccion_mecanica'),
    path('<str:dominio>/mecanica/eliminar/<int:pk>/', InspeccionMecanicaDeleteView.as_view(), name='eliminar_inspeccion_mecanica'),

    # 🚗 Inspección Exterior
    path('<str:dominio>/exterior/nueva/', InspeccionExteriorCreateView.as_view(), name='crear_inspeccion_exterior'),
    path('<str:dominio>/exterior/editar/<int:pk>/', InspeccionExteriorUpdateView.as_view(), name='editar_inspeccion_exterior'),
    path('<str:dominio>/exterior/eliminar/<int:pk>/', InspeccionExteriorDeleteView.as_view(), name='eliminar_inspeccion_exterior'),

    # 🛋 Inspección Interior
    path('<str:dominio>/interior/nueva/', InspeccionInteriorCreateView.as_view(), name='crear_inspeccion_interior'),
    path('<str:dominio>/interior/editar/<int:pk>/', InspeccionInteriorUpdateView.as_view(), name='editar_inspeccion_interior'),
    path('<str:dominio>/interior/eliminar/<int:pk>/', InspeccionInteriorDeleteView.as_view(), name='eliminar_inspeccion_interior'),
]
