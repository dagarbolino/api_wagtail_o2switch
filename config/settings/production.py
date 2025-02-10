import os
from .base import *  # noqa
from .base import BASE_DIR
from config import env

DEBUG = False

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/home/rahe9146/cheeseapi/logs/error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Configuration de l'API Wagtail
WAGTAILAPI_BASE_URL = "https://votre_domaine.com",
WAGTAILAPI_LIMIT_MAX = None

# Configuration CORS pour la production
CORS_ALLOWED_ORIGINS = [
    "https://votre_domaine.com",
    "https://www.votre_domaine.com",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'GET',
    'OPTIONS'
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'origin',
    'user-agent',
]

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

# Security configuration

# Ensure that the session cookie is only sent by browsers under an HTTPS connection.
# https://docs.djangoproject.com/en/stable/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True

# Ensure that the CSRF cookie is only sent by browsers under an HTTPS connection.
# https://docs.djangoproject.com/en/stable/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True

# Allow the redirect importer to work in load-balanced / cloud environments.
# https://docs.wagtail.io/en/v2.13/reference/settings.html#redirects
WAGTAIL_REDIRECTS_FILE_STORAGE = "cache"

# Force HTTPS redirect (enabled by default!)
SECURE_SSL_REDIRECT = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "no-referrer-when-downgrade"

# Configuration des fichiers statiques
STATIC_ROOT = env('DJANGO_STATIC_ROOT', default='/home/rahe9146/cheeseapi.alex-webdev.fr/static')
STATIC_URL = '/static/'
MEDIA_ROOT = env('DJANGO_MEDIA_ROOT', default='/home/rahe9146/cheeseapi.alex-webdev.fr/media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_compiled'),
]

# Configuration de Django-vite
DJANGO_VITE = {
    "default": {
        "dev_mode": False,
        "manifest_path": os.path.join(STATIC_ROOT, 'manifest.json'),
    },
}

# Utilisez FileSystemStorage
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Désactivez la compression des fichiers statiques
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
