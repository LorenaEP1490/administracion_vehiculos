from django.db import models

class Vehiculo(models.Model):
    dominio = models.CharField(max_length=10, unique=True)  # La clave principal de referencia
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.PositiveIntegerField()
    version = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=30)
    kilometros = models.PositiveIntegerField()
    tipo_combustible = models.CharField(max_length=20, choices=[('Nafta', 'Nafta'), ('Diesel', 'Diesel'), ('Nafta/GNC', 'Nafta/GNC')])
    transmision = models.CharField(max_length=20, choices=[('Manual', 'Manual'), ('Automático', 'Automático')])
    observaciones = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.dominio})"
