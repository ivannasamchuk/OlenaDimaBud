import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
import os
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "секрет_для_локального_запуску")
DEBUG = True
ALLOWED_HOSTS = ['.onrender.com']
INSTALLED_APPS = ['django.contrib.staticfiles']
MIDDLEWARE = []
ROOT_URLCONF = 'OlenaDimaBud.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {},
    },
]
WSGI_APPLICATION = 'OlenaDimaBud.wsgi.application'
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
import os

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
