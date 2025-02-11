from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import InspeccionAccesorios, InspeccionMecanica, InspeccionExterior, InspeccionInterior
from apps.vehiculos.models import Vehiculo

# 🛠 Vista para listar todas las inspecciones de un vehículo por dominio
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

### 🔧 **Inspección de Accesorios**
class InspeccionAccesoriosCreateView(CreateView):
    model = InspeccionAccesorios
    fields = "__all__"
    template_name = "inspecciones/crear_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})

class InspeccionAccesoriosUpdateView(UpdateView):
    model = InspeccionAccesorios
    fields = "__all__"
    template_name = "inspecciones/editar_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})

class InspeccionAccesoriosDeleteView(DeleteView):
    model = InspeccionAccesorios
    template_name = "inspecciones/eliminar_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})

### 🔧 **Inspección Mecánica**
class InspeccionMecanicaCreateView(CreateView):
    model = InspeccionMecanica
    fields = "__all__"
    template_name = "inspecciones/crear_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})

class InspeccionMecanicaUpdateView(UpdateView):
    model = InspeccionMecanica
    fields = "__all__"
    template_name = "inspecciones/editar_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})

class InspeccionMecanicaDeleteView(DeleteView):
    model = InspeccionMecanica
    template_name = "inspecciones/eliminar_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})

### 🚗 **Inspección Exterior**
class InspeccionExteriorCreateView(CreateView):
    model = InspeccionExterior
    fields = "__all__"
    template_name = "inspecciones/crear_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})

class InspeccionExteriorUpdateView(UpdateView):
    model = InspeccionExterior
    fields = "__all__"
    template_name = "inspecciones/editar_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})

class InspeccionExteriorDeleteView(DeleteView):
    model = InspeccionExterior
    template_name = "inspecciones/eliminar_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})

### 🛋 **Inspección Interior**
class InspeccionInteriorCreateView(CreateView):
    model = InspeccionInterior
    fields = "__all__"
    template_name = "inspecciones/crear_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})

class InspeccionInteriorUpdateView(UpdateView):
    model = InspeccionInterior
    fields = "__all__"
    template_name = "inspecciones/editar_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})

class InspeccionInteriorDeleteView(DeleteView):
    model = InspeccionInterior
    template_name = "inspecciones/eliminar_inspeccion.html"

    def get_success_url(self):
        return reverse_lazy("lista_inspecciones", kwargs={"dominio": self.object.vehiculo.dominio})
