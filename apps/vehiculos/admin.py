from django.contrib import admin
from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('dominio', 'marca', 'modelo', 'año', 'kilometros', 'tipo_combustible', 'transmision')
    search_fields = ('dominio', 'marca', 'modelo')
    list_filter = ('tipo_combustible', 'transmision', 'año')
