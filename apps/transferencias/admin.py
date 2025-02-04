from django.contrib import admin
from .models import Transferencia

@admin.register(Transferencia)
class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'comprador', 'fecha_transferencia', 'estado')
    search_fields = ('vehiculo__dominio', 'comprador')
    list_filter = ('estado', 'fecha_transferencia')
