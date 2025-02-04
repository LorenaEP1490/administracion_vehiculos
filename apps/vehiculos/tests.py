from django.test import TestCase
from .models import Vehiculo

class VehiculoTest(TestCase):
    def setUp(self):
        self.vehiculo = Vehiculo.objects.create(
            dominio="ABC123",
            marca="Toyota",
            modelo="Corolla",
            año=2020,
            color="Blanco",
            kilometros=50000,
            tipo_combustible="Nafta",
            transmision="Automático"
        )

    def test_creacion_vehiculo(self):
        """Prueba que el vehículo se haya creado correctamente"""
        self.assertEqual(self.vehiculo.dominio, "ABC123")
        self.assertEqual(self.vehiculo.marca, "Toyota")
        self.assertEqual(self.vehiculo.modelo, "Corolla")
        self.assertEqual(self.vehiculo.año, 2020)
        self.assertEqual(self.vehiculo.color, "Blanco")

    def test_str_method(self):
        """Prueba que el método __str__ devuelve el formato correcto"""
        self.assertEqual(str(self.vehiculo), "Toyota Corolla (ABC123)")
