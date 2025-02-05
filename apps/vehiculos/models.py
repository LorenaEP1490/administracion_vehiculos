from django.db import models

class Vehiculo(models.Model):
    dominio = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    version = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=30)
    kilometros = models.IntegerField()
    tipo_combustible = models.CharField(
        max_length=10,
        choices=[("Nafta", "Nafta"), ("Diesel", "Diesel"), ("Nafta/GNC", "Nafta/GNC")],
    )
    transmision = models.CharField(
        max_length=10,
        choices=[("Manual", "Manual"), ("Automático", "Automático")],
    )
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.dominio})"
