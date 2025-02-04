from django.test import TestCase
from apps.vehiculos.models import Vehiculo
from .models import Gasto

class GastoTest(TestCase):
    def setUp(self):
        self.vehiculo = Vehiculo.objects.create(
            dominio="XYZ123",
            marca="Honda",
            modelo="Civic",
            año=2019,
            color="Negro",
            kilometros=30000,
            tipo_combustible="Nafta",
            transmision="Automático"
        )
        self.gasto = Gasto.objects.create(
            vehiculo=self.vehiculo,
            detalle="Cambio de aceite",
            monto=5000,
            tipo="Reparación"
        )

    def test_creacion_gasto(self):
        """Prueba que el gasto se haya creado correctamente"""
        self.assertEqual(self.gasto.vehiculo.dominio, "XYZ123")
        self.assertEqual(self.gasto.detalle, "Cambio de aceite")
        self.assertEqual(self.gasto.monto, 5000)
        self.assertEqual(self.gasto.tipo, "Reparación")

    def test_str_method(self):
        """Prueba que el método __str__ devuelve el formato correcto"""
        self.assertEqual(str(self.gasto), "XYZ123 - Cambio de aceite ($5000.00)")
