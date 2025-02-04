from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Transferencia
from apps.vehiculos.models import Vehiculo

class TransferenciaListView(ListView):
    template_name = "transferencias/lista_transferencias.html"
    context_object_name = "transferencias"

    def get_queryset(self):
        dominio = self.kwargs.get("dominio")
        vehiculo = get_object_or_404(Vehiculo, dominio=dominio)
        return Transferencia.objects.filter(vehiculo=vehiculo)

class TransferenciaCreateView(CreateView):
    model = Transferencia
    fields = "__all__"
    template_name = "transferencias/crear_transferencia.html"
    success_url = reverse_lazy("lista_transferencias")

class TransferenciaUpdateView(UpdateView):
    model = Transferencia
    fields = "__all__"
    template_name = "transferencias/editar_transferencia.html"
    success_url = reverse_lazy("lista_transferencias")

class TransferenciaDeleteView(DeleteView):
    model = Transferencia
    template_name = "transferencias/eliminar_transferencia.html"
    success_url = reverse_lazy("lista_transferencias")
