import pymysql
import os
from pathlib import Path
from django.urls import reverse_lazy
import dj_database_url
from decouple import config

pymysql.install_as_MySQLdb()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xd3gl(zxlj5qct3h%=7g#c!@mpxaazb$w0ikxwsz_!+5(%i6ru'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# LOGIN 
LOGIN_REDIRECT_URL = reverse_lazy("inicio")
LOGIN_URL = reverse_lazy("login")
AUTH_USER_MODEL = "usuarios.Usuario"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.articulos',
    'apps.usuarios',
    'apps.categorias',
    'apps.comentarios',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'decadadeaccion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

WSGI_APPLICATION = 'decadadeaccion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASE_URL = 'postgres://uqbpjflyeqrlzr:89fa19e09f2127db11ff9ca3b6ba9691bee44fb3a450ec1b9ba9154c408ac742@ec2-54-225-203-79.compute-1.amazonaws.com:5432/d2vmb0pgh3bj6u'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "d2vmb0pgh3bj6u",
        "USER": "uqbpjflyeqrlzr",
        "PASSWORD": "89fa19e09f2127db11ff9ca3b6ba9691bee44fb3a450ec1b9ba9154c408ac742",
        "HOST": "ec2-54-225-203-79.compute-1.amazonaws.com",
        "PORT": "5432"
    },
    'default1': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "decadadeaccion",
        "USER": "root",
        "PASSWORD": "clave1234",
        "HOST": "localhost",
        "PORT": "3306"
    }
    
}

DATABASES['default2'] = dj_database_url.config(default='postgres://uqbpjflyeqrlzr:89fa19e09f2127db11ff9ca3b6ba9691bee44fb3a450ec1b9ba9154c408ac742@ec2-54-225-203-79.compute-1.amazonaws.com:5432/d2vmb0pgh3bj6u')

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    )

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
