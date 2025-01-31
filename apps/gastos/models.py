from django.db import models
from apps.vehiculos.models import Vehiculo

class Gasto(models.Model):
    TIPO_GASTO = [
        ('Reparación', 'Reparación'),
        ('Administrativo', 'Administrativo'),
        ('Otro', 'Otro'),
    ]

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    detalle = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=TIPO_GASTO)

    def __str__(self):
        return f"{self.vehiculo.dominio} - {self.detalle} (${self.monto})"
