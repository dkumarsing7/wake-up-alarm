import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Static files settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'alarm_theme', 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, default='sqlite:///db.sqlite3')

SECRET_KEY = 'django-insecure-bki5vif_1hcg*6mstbxxhl8o52(9#_*$4*07bil5%+!yn=)^s='

DEBUG = True

# Allowed hosts
ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1', 'localhost']

# NPM bin path
NPM_BIN_PATH = r'C:\Program Files\nodejs\npm.cmd'








# import os
# from pathlib import Path
# import dj_database_url
# BASE_DIR = Path(__file__).resolve().parent.parent

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, default='sqlite:///db.sqlite3')
# SECRET_KEY = 'django-insecure-bki5vif_1hcg*6mstbxxhl8o52(9#_*$4*07bil5%+!yn=)^s='

# DEBUG = True

# # settings.py
# ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1', 'localhost']



# INSTALLED_APPS = [
#     'tailwind',
#     'alarm_theme',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# ]
# TAILWIND_APP_NAME = 'alarm_theme'

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'WakeUpAlarm.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'WakeUpAlarm.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True



# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# NPM_BIN_PATH = r'C:\Program Files\nodejs\npm.cmd'