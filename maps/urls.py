from django.conf.urls import patterns, include, url
from maps.login import Login

urlpatterns = patterns(
    'maps.views',

    # base
    url(r'^$', 'base', name='base'),

    # cache manifest
    url(r'^cache\.manifest$', 'manifest', name='cache_manifest'),

    # angular templates
    url(r'^ng/templates/login$', Login.as_view(), name='ng_login'),
    url(r'^ng/templates/logout$', 'ng_logout', name='ng_logout'),
    url(r'^ng/templates/dashboard$', 'ng_dashboard', name='ng_dashboard'),
    url(r'^ng/templates/add-route$', 'ng_add_route', name='ng_add_route'),
    url(r'^ng/templates/route$', 'ng_route', name='ng_route'),

    # retrieve surveys
    url(r'^surveys/items$', 'survey_items', name='survey_items'),
)
