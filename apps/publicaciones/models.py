from django.db import models
from apps.vehiculos.models import Vehiculo

class Publicacion(models.Model):
    PLATAFORMAS = [
        ('MercadoLibre', 'MercadoLibre'),
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('WhatsApp', 'WhatsApp'),
        ('Otro', 'Otro'),
    ]
    
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(max_length=10, choices=[('Pesos', 'Pesos'), ('Dólares', 'Dólares')])
    plataforma = models.CharField(max_length=50, choices=PLATAFORMAS)
    fecha_publicacion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('Activa', 'Activa'), ('Vendida', 'Vendida'), ('Inactiva', 'Inactiva')], default='Activa')
    
    def __str__(self):
        return f"{self.vehiculo.dominio} - {self.plataforma} - ${self.precio}"
