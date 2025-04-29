SECRET_KEY = 'fake-key'
DEBUG = True
ALLOWED_HOSTS = ['*']
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
