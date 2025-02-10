from .base import *  # noqa F403
from .base import BASE_DIR
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATICFILES_DIRS = [
    BASE_DIR / "public",
]

# Configuration of Django-vite
DJANGO_VITE = {
    "default": {"dev_mode": True},
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7(%p2k9h*lfh*zk_t9wh2arum15gua20+05#48e)g#7vu2brz%"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Configuration de l'API Wagtail pour le développement
WAGTAILAPI_BASE_URL = 'http://localhost:8000'

# Configuration des CORS pour le développement
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Désactivez certaines sécurités en développement
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

# Configuration du cache des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

# Configuration de la base de données pour le développement
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'OPTIONS': {
            'timeout': 20,  # Augmente le timeout
        }
    }
}

try:
    from .local import *
except ImportError:
    pass
