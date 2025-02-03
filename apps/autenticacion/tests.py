from django.test import TestCase
from django.contrib.auth import get_user_model

class AutenticacionTest(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword",
            rol="usuario"
        )

    def test_creacion_usuario(self):
        """Verifica que el usuario se crea correctamente"""
        self.assertEqual(self.usuario.username, "testuser")
        self.assertEqual(self.usuario.email, "test@example.com")
        self.assertTrue(self.usuario.check_password("testpassword"))

    def test_login_usuario(self):
        """Verifica que el usuario puede iniciar sesión"""
        login_exitoso = self.client.login(username="testuser", password="testpassword")
        self.assertTrue(login_exitoso)

    def test_logout_usuario(self):
        """Verifica que el usuario puede cerrar sesión"""
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get("/logout/")
        self.assertEqual(response.status_code, 302)  # Redirección tras cerrar sesión
