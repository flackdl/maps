from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # custom group
        self.children.append(modules.LinkList(
            _('Links'),
            column=2,
            children=[
                {
                    'title': _('MAPS App'),
                    'url': reverse('base'),
                    'external': True,
                },
                {
                    'title': _('Batch Import Entries'),
                    'url': reverse('import_entries'),
                },
            ]
        ))

        self.children.append(modules.ModelList(
            title='Surveys and Entries',
            column=1,
            models=('maps.models.Survey', 'entries.models.Entry'),
            pre_content='<h4>Create surveys and assign user entries</h4>'
        ))

        self.children.append(modules.AppList(
            _('Administration'),
            column=1,
            models=('django.contrib.*',),
            #models=('django.contrib.sites.models.Site',),
            exclude=('django.contrib.sites.models.Site',),
            pre_content='<h4>Manage users, groups and permissions</h4>'
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=10,
            collapsible=False,
            column=3,
        ))


