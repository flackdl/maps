from django.conf.urls import patterns, include, url
from entries.submission import Submit, Retrieve
from entries.export import Export
from entries.import_ import Import

urlpatterns = patterns(
    'entries.views',

    url(r'^submit', Submit.as_view()),
    url(r'^retrieve', Retrieve.as_view()),

    # export
    url(r'export$', Export.as_view(), name='export_entries'),
    url(r'export/in-browser$', Export.as_view(render_in_browser=True), name='export_entries_browser'),

    # import
    url(r'import$', Import.as_view(), name='import_entries'),
)
