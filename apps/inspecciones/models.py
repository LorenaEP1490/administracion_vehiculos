from django.db import models
from apps.vehiculos.models import Vehiculo

OPCIONES_SI_NO = [
    ("si", "Sí"),
    ("no", "No"),
]

OPCIONES_ESTADO = [
    ("bueno", "Buen Estado"),
    ("danado", "Dañado"),
    ("atencion", "Requiere Atención"),
]

OPCIONES_FUNCIONA = [
    ("funciona", "Funciona"),
    ("no_funciona", "No Funciona"),
]

class InspeccionAccesorios(models.Model):
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE, related_name="inspeccion_accesorios")
    cricket = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default="no")
    matafuegos = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default="no")
    stereo = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default="no")
    stereo_funciona = models.CharField(max_length=12, choices=OPCIONES_FUNCIONA, default="funciona")
    stereo_marca = models.CharField(max_length=50, blank=True, null=True)
    navegador = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default="no")
    bateria = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default="no")
    bateria_marca = models.CharField(max_length=50, blank=True, null=True)
    bateria_amperaje = models.CharField(max_length=20, blank=True, null=True)
    tuercas_seguridad = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default="no")
    manuales = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default="no")
    duplicado_llaves = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default="no")
    observaciones = models.TextField(blank=True, null=True)

class InspeccionMecanica(models.Model):
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE, related_name="inspeccion_mecanica")
    motor = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    motor_observaciones = models.TextField(blank=True, null=True)
    niveles_liquidos = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    bateria_estado = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    transmision = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    frenos = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    suspension = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    escape = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    emisiones = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    arranque_motor = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    radiador = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    embrague = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")

class InspeccionExterior(models.Model):
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE, related_name="inspeccion_exterior")
    carroceria = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default="no")
    carroceria_detalle = models.TextField(blank=True, null=True)
    pintura = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default="no")
    pintura_detalle = models.TextField(blank=True, null=True)
    parabrisas = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default="no")
    parabrisas_detalle = models.TextField(blank=True, null=True)
    faros = models.CharField(max_length=2, choices=OPCIONES_SI_NO, default="no")
    faros_detalle = models.TextField(blank=True, null=True)
    neumaticos = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    espejos = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    limpiaparabrisas = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")

class InspeccionInterior(models.Model):
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE, related_name="inspeccion_interior")
    asientos = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    tablero = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    climatizacion = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    audio = models.CharField(max_length=12, choices=OPCIONES_FUNCIONA, default="funciona")
    audio_observaciones = models.TextField(blank=True, null=True)
    alfombras = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="bueno")
    airbag = models.CharField(max_length=12, choices=OPCIONES_FUNCIONA, default="funciona")
    airbag_observaciones = models.TextField(blank=True, null=True)
