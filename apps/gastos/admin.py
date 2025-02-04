from django.contrib import admin
from .models import Gasto

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'fecha', 'detalle', 'monto', 'tipo')
    search_fields = ('vehiculo__dominio', 'detalle')
    list_filter = ('tipo', 'fecha')
