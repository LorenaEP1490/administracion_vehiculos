from django.urls import path
from .views import GastoListView, GastoCreateView, GastoUpdateView, GastoDeleteView

urlpatterns = [
    path('<str:dominio>/', GastoListView.as_view(), name='lista_gastos'),
    path('nuevo/', GastoCreateView.as_view(), name='crear_gasto'),
    path('editar/<int:pk>/', GastoUpdateView.as_view(), name='editar_gasto'),
    path('eliminar/<int:pk>/', GastoDeleteView.as_view(), name='eliminar_gasto'),
]
