from django.db import models
from apps.vehiculos.models import Vehiculo

class Transferencia(models.Model):
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
    comprador = models.CharField(max_length=100)
    dni_comprador = models.CharField(max_length=10)
    fecha_transferencia = models.DateField()
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Finalizada', 'Finalizada')])
    
    def __str__(self):
        return f"Transferencia {self.vehiculo.dominio} - {self.estado}"
