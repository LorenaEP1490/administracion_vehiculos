import os
from pathlib import Path

# BASE DIR: Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = 'django-insecure-tu_clave_secreta_aqui'
DEBUG = True  # Cambia a False en producción
ALLOWED_HOSTS = [
    "127.0.0.1", 
    "localhost",
    "0.0.0.0",  # Para evitar problemas en Codespaces
]

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Aplicaciones del proyecto dentro de "apps/"
    'apps.autenticacion',
    'apps.vehiculos',
    'apps.inspecciones',
    'apps.gastos',
    'apps.publicaciones',
    'apps.transferencias',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Necesario para autenticación y admin
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Necesario para autenticación
    'django.contrib.messages.middleware.MessageMiddleware',  # Necesario para mensajes en admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL principal del proyecto
ROOT_URLCONF = 'gestion_vehiculos.urls'

# Configuración de Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Carpeta global de templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuración WSGI
WSGI_APPLICATION = 'gestion_vehiculos.wsgi.application'

# Configuración de la Base de Datos (SQLite por defecto, puedes cambiar a PostgreSQL o MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración de autenticación
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Modelo de usuario personalizado
AUTH_USER_MODEL = "autenticacion.Usuario"

# Configuración de localización
LANGUAGE_CODE = 'es-ar'  # Español Argentina
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuración de archivos de medios (para subir imágenes o documentos)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración por defecto del campo de clave primaria
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de LOGIN y LOGOUT
LOGIN_URL = "/auth/login/"
LOGOUT_REDIRECT_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/"

# Protege el sistema contra ataques CSRF
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "https://127.0.0.1:8000",
    "https://localhost:8000",
]

# Redirección de usuarios no autenticados
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Cierra sesión al cerrar el navegador
SESSION_COOKIE_AGE = 3600  # Expira la sesión en 1 hora (ajustable)
SESSION_SAVE_EVERY_REQUEST = True  # Refresca la sesión en cada solicitud
