from django.db import models
from apps.vehiculos.models import Vehiculo

# 1️⃣ Inspección de Accesorios
class InspeccionAccesorios(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    responsable = models.CharField(max_length=100)

    # Accesorios
    cricket = models.BooleanField(default=False)
    matafuegos = models.BooleanField(default=False)
    stereo = models.BooleanField(default=False)
    navegador = models.BooleanField(default=False)
    bateria = models.BooleanField(default=False)
    tuercas_seguridad = models.BooleanField(default=False)
    manuales = models.BooleanField(default=False)
    duplicado_llaves = models.BooleanField(default=False)
    
    # Cubiertas
    cubierta_DI_marca = models.CharField(max_length=50, blank=True, null=True)
    cubierta_DI_rodado = models.CharField(max_length=20, blank=True, null=True)
    cubierta_DD_marca = models.CharField(max_length=50, blank=True, null=True)
    cubierta_DD_rodado = models.CharField(max_length=20, blank=True, null=True)
    cubierta_TI_marca = models.CharField(max_length=50, blank=True, null=True)
    cubierta_TI_rodado = models.CharField(max_length=20, blank=True, null=True)
    cubierta_TD_marca = models.CharField(max_length=50, blank=True, null=True)
    cubierta_TD_rodado = models.CharField(max_length=20, blank=True, null=True)
    auxilio_marca = models.CharField(max_length=50, blank=True, null=True)
    auxilio_rodado = models.CharField(max_length=20, blank=True, null=True)
    
    # Batería
    bateria_marca = models.CharField(max_length=50, blank=True, null=True)
    bateria_amperaje = models.IntegerField(blank=True, null=True)

    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Inspección de Accesorios - {self.vehiculo.dominio}"

# 2️⃣ Inspección Mecánica
class InspeccionMecanica(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    responsable = models.CharField(max_length=100)

    motor = models.BooleanField(default=False)
    niveles_liquidos = models.BooleanField(default=False)
    bateria = models.BooleanField(default=False)
    transmision = models.BooleanField(default=False)
    frenos = models.BooleanField(default=False)
    suspension = models.BooleanField(default=False)
    escape = models.BooleanField(default=False)
    revision_emisiones = models.BooleanField(default=False)
    arranque_motor = models.BooleanField(default=False)
    radiador = models.BooleanField(default=False)
    estado_embrague = models.BooleanField(default=False)

    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Inspección Mecánica - {self.vehiculo.dominio}"

# 3️⃣ Inspección Exterior
class InspeccionExterior(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    responsable = models.CharField(max_length=100)

    carroceria = models.BooleanField(default=False)
    pintura = models.BooleanField(default=False)
    parabrisas_ventanas = models.BooleanField(default=False)
    faros_luces = models.BooleanField(default=False)
    neumaticos = models.BooleanField(default=False)
    espejos_retrovisores = models.BooleanField(default=False)
    limpiaparabrisas = models.BooleanField(default=False)

    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Inspección Exterior - {self.vehiculo.dominio}"

# 4️⃣ Inspección Interior
class InspeccionInterior(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    responsable = models.CharField(max_length=100)

    asientos = models.BooleanField(default=False)
    tablero = models.BooleanField(default=False)
    climatizacion = models.BooleanField(default=False)
    sistema_audio = models.BooleanField(default=False)
    alfombras_tapetes = models.BooleanField(default=False)
    airbag = models.BooleanField(default=False)

    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Inspección Interior - {self.vehiculo.dominio}"
