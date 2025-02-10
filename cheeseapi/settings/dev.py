from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Configuration of Django-vite
DJANGO_VITE = {
    "default": {"dev_mode": True},
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7(%p2k9h*lfh*zk_t9wh2arum15gua20+05#48e)g#7vu2brz%"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

try:
    from .local import *
except ImportError:
    pass
