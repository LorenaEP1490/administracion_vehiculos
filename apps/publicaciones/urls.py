from django.urls import path
from .views import PublicacionListView, PublicacionCreateView, PublicacionUpdateView, PublicacionDeleteView

urlpatterns = [
    path('<str:dominio>/', PublicacionListView.as_view(), name='lista_publicaciones'),
    path('nueva/', PublicacionCreateView.as_view(), name='crear_publicacion'),
    path('editar/<int:pk>/', PublicacionUpdateView.as_view(), name='editar_publicacion'),
    path('eliminar/<int:pk>/', PublicacionDeleteView.as_view(), name='eliminar_publicacion'),
]
