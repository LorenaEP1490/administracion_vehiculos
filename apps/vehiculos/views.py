from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Vehiculo
from .forms import VehiculoForm

# Vista para listar todos los vehículos
@login_required
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, "vehiculos/lista_vehiculos.html", {"vehiculos": vehiculos})

# Vista para crear un nuevo vehículo
@login_required
def crear_vehiculo(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_vehiculos")  # Redirigir después de guardar
    else:
        form = VehiculoForm()
    return render(request, "vehiculos/crear_vehiculo.html", {"form": form})

# Vista para editar un vehículo existente
@login_required
def editar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == "POST":
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect("lista_vehiculos")
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, "vehiculos/editar_vehiculo.html", {"form": form, "vehiculo": vehiculo})

# Vista para eliminar un vehículo
@login_required
def eliminar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == "POST":
        vehiculo.delete()
        return redirect("lista_vehiculos")
    return render(request, "vehiculos/eliminar_vehiculo.html", {"vehiculo": vehiculo})

# Vista para buscar un vehículo por dominio (AJAX)
@login_required
def buscar_vehiculo(request, dominio):
    try:
        vehiculo = Vehiculo.objects.get(dominio=dominio)
        return JsonResponse({
            "existe": True,
            "marca": vehiculo.marca,
            "modelo": vehiculo.modelo,
            "año": vehiculo.año,
        })
    except Vehiculo.DoesNotExist:
        return JsonResponse({"existe": False})
