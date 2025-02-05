from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import InspeccionAccesorios, InspeccionMecanica, InspeccionExterior, InspeccionInterior
from apps.vehiculos.models import Vehiculo

# Vista para listar inspecciones de un vehículo por dominio
class InspeccionListView(ListView):
    template_name = "inspecciones/lista_inspecciones.html"
    context_object_name = "inspecciones"

    def get_queryset(self):
        dominio = self.kwargs.get("dominio")
        vehiculo = get_object_or_404(Vehiculo, dominio=dominio)
        return {
            "accesorios": InspeccionAccesorios.objects.filter(vehiculo=vehiculo),
            "mecanica": InspeccionMecanica.objects.filter(vehiculo=vehiculo),
            "exterior": InspeccionExterior.objects.filter(vehiculo=vehiculo),
            "interior": InspeccionInterior.objects.filter(vehiculo=vehiculo),
        }

# Vista para crear una inspección de accesorios
class InspeccionAccesoriosCreateView(CreateView):
    model = InspeccionAccesorios
    fields = "__all__"
    template_name = "inspecciones/crear_inspeccion.html"
    success_url = reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})


# Vista para actualizar una inspección de accesorios
class InspeccionAccesoriosUpdateView(UpdateView):
    model = InspeccionAccesorios
    fields = "__all__"
    template_name = "inspecciones/editar_inspeccion.html"
    success_url = reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})


# Vista para eliminar una inspección de accesorios
class InspeccionAccesoriosDeleteView(DeleteView):
    model = InspeccionAccesorios
    template_name = "inspecciones/eliminar_inspeccion.html"
    success_url = reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})

