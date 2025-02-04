from django.test import TestCase
from apps.vehiculos.models import Vehiculo
from .models import Transferencia

class TransferenciaTest(TestCase):
    def setUp(self):
        self.vehiculo = Vehiculo.objects.create(
            dominio="AAA111",
            marca="Chevrolet",
            modelo="Cruze",
            año=2021,
            color="Gris",
            kilometros=15000,
            tipo_combustible="Nafta",
            transmision="Automático"
        )
        self.transferencia = Transferencia.objects.create(
            vehiculo=self.vehiculo,
            comprador="Juan Pérez",
            dni_comprador="12345678",
            fecha_transferencia="2025-02-05",
            estado="Pendiente"
        )

    def test_creacion_transferencia(self):
        """Prueba que la transferencia se haya creado correctamente"""
        self.assertEqual(self.transferencia.vehiculo.dominio, "AAA111")
        self.assertEqual(self.transferencia.comprador, "Juan Pérez")
        self.assertEqual(self.transferencia.estado, "Pendiente")

    def test_str_method(self):
        """Prueba que el método __str__ devuelve el formato correcto"""
        self.assertEqual(str(self.transferencia), "Transferencia AAA111 - Pendiente")
