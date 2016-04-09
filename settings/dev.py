from settings.common import *

DEBUG = True

HTML_APP_CACHE = False

INSTALLED_APPS += (
    #'debug_toolbar',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'alr',
        'USER': 'dev',
        'PASSWORD': 'dev',
        'HOST': '127.0.0.1',
        'OPTIONS': {'init_command': 'SET storage_engine=INNODB;'},
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
