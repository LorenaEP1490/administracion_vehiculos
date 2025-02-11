from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import InspeccionAccesorios, InspeccionMecanica, InspeccionExterior, InspeccionInterior
from apps.vehiculos.models import Vehiculo

# 🛠 Vista para listar todas las inspecciones de un vehículo por dominio
class InspeccionListView(ListView):
    template_name = "inspecciones/lista_inspecciones.html"
    context_object_name = "inspecciones"

    def get_queryset(self):
        dominio = self.kwargs.get("dominio")
        self.vehiculo = get_object_or_404(Vehiculo, dominio=dominio)
        return {
            "accesorios": InspeccionAccesorios.objects.filter(vehiculo=self.vehiculo),
            "mecanica": InspeccionMecanica.objects.filter(vehiculo=self.vehiculo),
            "exterior": InspeccionExterior.objects.filter(vehiculo=self.vehiculo),
            "interior": InspeccionInterior.objects.filter(vehiculo=self.vehiculo),
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehiculo"] = self.vehiculo
        return context


### 🔧 **Inspección de Accesorios**
class InspeccionAccesoriosCreateView(CreateView):
    model = InspeccionAccesorios
    fields = "__all__"
    template_name = "inspecciones/crear_inspeccion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehiculo"] = get_object_or_404(Vehiculo, dominio=self.kwargs.get("dominio"))
        return context

    def form_valid(self, form):
        form.instance.vehiculo = get_object_or_404(Vehiculo, dominio=self.kwargs.get("dominio"))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})


### 🔧 **Inspección Mecánica**
class InspeccionMecanicaCreateView(InspeccionAccesoriosCreateView):
    model = InspeccionMecanica


### 🚗 **Inspección Exterior**
class InspeccionExteriorCreateView(InspeccionAccesoriosCreateView):
    model = InspeccionExterior


### 🛋 **Inspección Interior**
class InspeccionInteriorCreateView(InspeccionAccesoriosCreateView):
    model = InspeccionInterior


# **Actualizar Inspecciones**
class InspeccionAccesoriosUpdateView(UpdateView):
    model = InspeccionAccesorios
    fields = "__all__"
    template_name = "inspecciones/editar_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})


class InspeccionMecanicaUpdateView(InspeccionAccesoriosUpdateView):
    model = InspeccionMecanica


class InspeccionExteriorUpdateView(InspeccionAccesoriosUpdateView):
    model = InspeccionExterior


class InspeccionInteriorUpdateView(InspeccionAccesoriosUpdateView):
    model = InspeccionInterior


# **Eliminar Inspecciones**
class InspeccionAccesoriosDeleteView(DeleteView):
    model = InspeccionAccesorios
    template_name = "inspecciones/eliminar_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})


class InspeccionMecanicaDeleteView(InspeccionAccesoriosDeleteView):
    model = InspeccionMecanica


class InspeccionExteriorDeleteView(InspeccionAccesoriosDeleteView):
    model = InspeccionExterior


class InspeccionInteriorDeleteView(InspeccionAccesoriosDeleteView):
    model = InspeccionInterior
