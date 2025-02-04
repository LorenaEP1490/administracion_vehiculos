from django.urls import path
from .views import TransferenciaListView, TransferenciaCreateView, TransferenciaUpdateView, TransferenciaDeleteView

urlpatterns = [
    path('<str:dominio>/', TransferenciaListView.as_view(), name='lista_transferencias'),
    path('nueva/', TransferenciaCreateView.as_view(), name='crear_transferencia'),
    path('editar/<int:pk>/', TransferenciaUpdateView.as_view(), name='editar_transferencia'),
    path('eliminar/<int:pk>/', TransferenciaDeleteView.as_view(), name='eliminar_transferencia'),
]
