from django.conf import settings
from django.conf.urls import patterns, include, url
from filebrowser.sites import site as filebrowser_site
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^', include('maps.urls')),
    url(r'^entries/', include('entries.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include(filebrowser_site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)

# Development only - serving user-uploaded files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
