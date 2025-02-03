from django.contrib import admin
from .models import InspeccionAccesorios, InspeccionMecanica, InspeccionExterior, InspeccionInterior

@admin.register(InspeccionAccesorios)
class InspeccionAccesoriosAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'fecha', 'responsable', 'cricket', 'matafuegos', 'stereo', 'navegador')
    search_fields = ('vehiculo__dominio', 'responsable')
    list_filter = ('fecha',)

@admin.register(InspeccionMecanica)
class InspeccionMecanicaAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'fecha', 'responsable', 'motor', 'niveles_liquidos', 'bateria', 'transmision')
    search_fields = ('vehiculo__dominio', 'responsable')
    list_filter = ('fecha',)

@admin.register(InspeccionExterior)
class InspeccionExteriorAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'fecha', 'responsable', 'carroceria', 'pintura', 'parabrisas_ventanas', 'faros_luces')
    search_fields = ('vehiculo__dominio', 'responsable')
    list_filter = ('fecha',)

@admin.register(InspeccionInterior)
class InspeccionInteriorAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'fecha', 'responsable', 'asientos', 'tablero', 'climatizacion', 'sistema_audio')
    search_fields = ('vehiculo__dominio', 'responsable')
    list_filter = ('fecha',)
