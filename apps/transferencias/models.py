from django.db import models
from apps.vehiculos.models import Vehiculo

class Transferencia(models.Model):
    ESTADO_TRANSFERENCIA = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Completada', 'Completada'),
    ]

    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
    comprador = models.CharField(max_length=100)
    dni_comprador = models.CharField(max_length=10)
    fecha_transferencia = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_TRANSFERENCIA, default='Pendiente')

    # Documentación requerida
    titulo_vehiculo = models.BooleanField(default=False)
    form_08 = models.BooleanField(default=False)
    cedula_verde = models.BooleanField(default=False)
    cedula_azul = models.BooleanField(default=False)
    verificacion_policial = models.BooleanField(default=False)
    informe_historico_dominio = models.BooleanField(default=False)
    cuil_cuit_comprador = models.BooleanField(default=False)
    dni_conyuge = models.BooleanField(default=False)

    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Transferencia {self.vehiculo.dominio} - {self.estado}"
