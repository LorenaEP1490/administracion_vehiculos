from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Vehiculo

class VehiculoListView(ListView):
    model = Vehiculo
    template_name = "vehiculos/lista_vehiculos.html"
    context_object_name = "vehiculos"

class VehiculoCreateView(CreateView):
    model = Vehiculo
    fields = "__all__"
    template_name = "vehiculos/crear_vehiculo.html"
    success_url = reverse_lazy("lista_vehiculos")

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    fields = "__all__"
    template_name = "vehiculos/editar_vehiculo.html"
    success_url = reverse_lazy("lista_vehiculos")

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    template_name = "vehiculos/eliminar_vehiculo.html"
    success_url = reverse_lazy("lista_vehiculos")
