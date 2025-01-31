from django.db import models
from apps.vehiculos.models import Vehiculo

class Publicacion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(max_length=10, choices=[('Pesos', 'Pesos'), ('Dólares', 'Dólares')])
    plataforma = models.CharField(max_length=50, choices=[('MercadoLibre', 'MercadoLibre'), ('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('WhatsApp', 'WhatsApp')])
    fecha_publicacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Publicación {self.vehiculo.dominio} en {self.plataforma} - ${self.precio}"
