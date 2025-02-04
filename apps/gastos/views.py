from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Gasto
from apps.vehiculos.models import Vehiculo

class GastoListView(ListView):
    template_name = "gastos/lista_gastos.html"
    context_object_name = "gastos"

    def get_queryset(self):
        dominio = self.kwargs.get("dominio")
        vehiculo = get_object_or_404(Vehiculo, dominio=dominio)
        return Gasto.objects.filter(vehiculo=vehiculo)

class GastoCreateView(CreateView):
    model = Gasto
    fields = "__all__"
    template_name = "gastos/crear_gasto.html"
    success_url = reverse_lazy("lista_gastos")

class GastoUpdateView(UpdateView):
    model = Gasto
    fields = "__all__"
    template_name = "gastos/editar_gasto.html"
    success_url = reverse_lazy("lista_gastos")

class GastoDeleteView(DeleteView):
    model = Gasto
    template_name = "gastos/eliminar_gasto.html"
    success_url = reverse_lazy("lista_gastos")
