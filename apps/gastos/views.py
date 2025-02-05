from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Gasto
from apps.vehiculos.models import Vehiculo

# 📌 Vista para listar los gastos de un vehículo por dominio
class GastoListView(ListView):
    template_name = "gastos/lista_gastos.html"
    context_object_name = "gastos"

    def get_queryset(self):
        dominio = self.kwargs.get("dominio")
        vehiculo = get_object_or_404(Vehiculo, dominio=dominio)
        return Gasto.objects.filter(vehiculo=vehiculo)

# 📌 Vista para crear un gasto
class GastoCreateView(CreateView):
    model = Gasto
    fields = "__all__"
    template_name = "gastos/crear_gasto.html"

    def get_success_url(self):
        return reverse_lazy("lista_gastos", kwargs={"dominio": self.object.vehiculo.dominio})

# 📌 Vista para editar un gasto
class GastoUpdateView(UpdateView):
    model = Gasto
    fields = "__all__"
    template_name = "gastos/editar_gasto.html"

    def get_success_url(self):
        return reverse_lazy("lista_gastos", kwargs={"dominio": self.object.vehiculo.dominio})

# 📌 Vista para eliminar un gasto
class GastoDeleteView(DeleteView):
    model = Gasto
    template_name = "gastos/eliminar_gasto.html"

    def get_success_url(self):
        return reverse_lazy("lista_gastos", kwargs={"dominio": self.object.vehiculo.dominio})
