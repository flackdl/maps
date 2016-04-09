"""
Django settings for alr project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS, DEBUG

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$gosoar$9zxe-p2*#g6#c)gmll%!m&!0db17+-9ss+gx)+@_9i'

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1']

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
    "maps.context_processors.maps_settings",
)

# Application definition

INSTALLED_APPS = (

    'grappelli.dashboard',  # custom dashboard
    'grappelli',  # needs to be before django.contrib.admin

    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'filebrowser',
    'south',

    # local apps
    'maps',
    'entries',
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'alr.urls'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

WSGI_APPLICATION = 'alr.wsgi.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

LOGIN_URL = 'ng_login'
LOGIN_REDIRECT_URL = 'base'
ACCOUNT_LOGOUT_REDIRECT_URL = 'base'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Grappelli https://django-grappelli.readthedocs.org/en/latest/
GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = 'MAPS'

# FileBrowser http://django-filebrowser.readthedocs.org/en/latest/settings.html#versions
FILEBROWSER_ADMIN_VERSIONS = []
FILEBROWSER_MAX_UPLOAD_SIZE = 153600  # 150kb
FILEBROWSER_SELECT_FORMATS = {
    'image': ['Image'],
    'document': ['Document'],
}
FILEBROWSER_EXTENSIONS = {
    'Image': ['.jpg', '.jpeg', '.gif', '.png'],
}

# MAJOR.MINOR.PATCH
MAPS_VERSION = '1.1.0'

# use html5 application cache if we're not in debug mode
HTML_APP_CACHE = not DEBUG
