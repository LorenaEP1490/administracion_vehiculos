from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Publicacion
from apps.vehiculos.models import Vehiculo

class PublicacionListView(ListView):
    template_name = "publicaciones/lista_publicaciones.html"
    context_object_name = "publicaciones"

    def get_queryset(self):
        dominio = self.kwargs.get("dominio")
        vehiculo = get_object_or_404(Vehiculo, dominio=dominio)
        return Publicacion.objects.filter(vehiculo=vehiculo)

class PublicacionCreateView(CreateView):
    model = Publicacion
    fields = "__all__"
    template_name = "publicaciones/crear_publicacion.html"
    success_url = reverse_lazy("lista_publicaciones")

class PublicacionUpdateView(UpdateView):
    model = Publicacion
    fields = "__all__"
    template_name = "publicaciones/editar_publicacion.html"
    success_url = reverse_lazy("lista_publicaciones")

class PublicacionDeleteView(DeleteView):
    model = Publicacion
    template_name = "publicaciones/eliminar_publicacion.html"
    success_url = reverse_lazy("lista_publicaciones")
