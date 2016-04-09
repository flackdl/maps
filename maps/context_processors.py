from django.conf import settings


def maps_settings(request):
    return {
        'MAPS_VERSION': settings.MAPS_VERSION,
        'HTML_APP_CACHE': settings.HTML_APP_CACHE,
    }
