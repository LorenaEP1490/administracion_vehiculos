from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('admin', 'Administrador'),
        ('usuario', 'Usuario'),
    ]
    
    rol = models.CharField(max_length=10, choices=ROLES, default='usuario')

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
