from django.contrib import admin
from .models import Publicacion

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'plataforma', 'precio', 'moneda', 'estado', 'fecha_publicacion')
    search_fields = ('vehiculo__dominio', 'plataforma')
    list_filter = ('estado', 'plataforma', 'fecha_publicacion')
