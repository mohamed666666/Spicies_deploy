"""
Django settings for Foodies project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from django.utils.translation import gettext_lazy as _
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG" , default=0))
DEBUG=True
#ALLOWED_HOSTS =os.environ.get("ALLOWED_HOSTS").split(" ")
ALLOWED_HOSTS=["*"]

# Application definition

INSTALLED_APPS = [
    "store.apps.StoreConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #"store",
    "basket",
    "user",
    "order",
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Foodies.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
 		        "store.views.categories",
                "basket.contex_processor.basket"
            ],
        },
    },
]

WSGI_APPLICATION = 'Foodies.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
     'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME":os.environ.get("NAME"),
        "USER":os.environ.get("USER"),
        "PASSWORD":os.environ.get("PASSWORD"),
        "HOST":os.environ.get("HOST"),
        "PORT":os.environ.get("PORT")
}
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


LANGUAGES = (
    ('en', _('English')),
    ('ar', _('Arabic'))
    )


LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field




SITE_ROOT = os.path.dirname(os.path.realpath(__file__))


APPS_DIR = os.path.join(BASE_DIR.parent,'nginx/')


MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'

STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'static')
       ]

STATIC_ROOT =  os.path.join(BASE_DIR, 'staticfiles')
# Stripe Payment
# PUBLISHABLE_KEY = ''
# SECRET_KEY = ''
# STRIPE_ENDPOINT_SECRET = ''
# stripe listen --forward-to localhost:8000/payment/webhook/

# Custom user model
AUTH_USER_MODEL = 'user.UserBase'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/user/login/'


PASSWORD_RESET_TIMEOUT_DAYS=2
# Email setting
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'vandetam97@gmail.com'
EMAIL_HOST_PASSWORD = '183492765'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
"""
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = ["http://34.239.123.66","http://0.0.0.0:85",'https://*.127.0.0.1:85']
