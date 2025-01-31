from django.db import models
from apps.vehiculos.models import Vehiculo

class Inspeccion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_inspeccion = models.DateField(auto_now_add=True)
    accesorios = models.TextField(blank=True, null=True)  # Lista de accesorios inspeccionados
    mecanica = models.TextField(blank=True, null=True)  # Resultados de inspección mecánica
    exterior = models.TextField(blank=True, null=True)  # Resultados de inspección exterior
    interior = models.TextField(blank=True, null=True)  # Resultados de inspección interior
    observaciones = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Inspección {self.vehiculo.dominio} - {self.fecha_inspeccion}"
