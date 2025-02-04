from django.test import TestCase
from apps.vehiculos.models import Vehiculo
from .models import Publicacion

class PublicacionTest(TestCase):
    def setUp(self):
        self.vehiculo = Vehiculo.objects.create(
            dominio="ZZZ999",
            marca="Ford",
            modelo="Focus",
            año=2022,
            color="Azul",
            kilometros=10000,
            tipo_combustible="Nafta",
            transmision="Manual"
        )
        self.publicacion = Publicacion.objects.create(
            vehiculo=self.vehiculo,
            precio=20000,
            moneda="Dólares",
            plataforma="Facebook",
            estado="Activa"
        )

    def test_creacion_publicacion(self):
        """Prueba que la publicación se haya creado correctamente"""
        self.assertEqual(self.publicacion.vehiculo.dominio, "ZZZ999")
        self.assertEqual(self.publicacion.precio, 20000)
        self.assertEqual(self.publicacion.moneda, "Dólares")
        self.assertEqual(self.publicacion.plataforma, "Facebook")
        self.assertEqual(self.publicacion.estado, "Activa")

    def test_str_method(self):
        """Prueba que el método __str__ devuelve el formato correcto"""
        self.assertEqual(str(self.publicacion), "ZZZ999 - Facebook - $20000.00")
