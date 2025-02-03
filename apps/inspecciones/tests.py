from django.test import TestCase
from apps.vehiculos.models import Vehiculo
from .models import InspeccionAccesorios

class InspeccionAccesoriosTest(TestCase):
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
        self.inspeccion = InspeccionAccesorios.objects.create(
            vehiculo=self.vehiculo,
            responsable="Inspector 1",
            cricket=True,
            matafuegos=True,
            stereo=True,
            navegador=False,
            bateria=True
        )

    def test_creacion_inspeccion(self):
        """Prueba que la inspección de accesorios se haya creado correctamente"""
        self.assertEqual(self.inspeccion.vehiculo.dominio, "ABC123")
        self.assertTrue(self.inspeccion.cricket)
        self.assertTrue(self.inspeccion.matafuegos)
        self.assertTrue(self.inspeccion.stereo)
        self.assertFalse(self.inspeccion.navegador)

    def test_str_method(self):
        """Prueba que el método __str__ devuelve el formato correcto"""
        self.assertEqual(str(self.inspeccion), "Inspección de Accesorios - ABC123")
