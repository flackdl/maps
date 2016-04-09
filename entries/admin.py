import urllib
from django.contrib import admin
from django.core.urlresolvers import reverse
from entries.models import Entry
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect


#########################
# List Filters
#########################
from maps.models import Survey


class RouteListFilter(admin.SimpleListFilter):
    title = ('Route #')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'route'

    def lookups(self, request, model_admin):
        return [(r, r) for r in set(Entry.objects.all().values_list('route_number', flat=True))]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(route_number=self.value())
        return queryset


class SurveyListFilter(admin.SimpleListFilter):
    title = ('Survey')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'survey'

    def lookups(self, request, model_admin):
        return [(s.id, s.version) for s in Survey.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(survey__id=self.value())
        return queryset


class AuditorListFilter(admin.SimpleListFilter):
    title = ('Auditor')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'auditor'

    def lookups(self, request, model_admin):
        return [(u.username, u.username) for u in User.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(auditor__username=self.value())
        return queryset


class CompletedListFilter(admin.SimpleListFilter):
    title = ('Completed')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'completed'

    def lookups(self, request, model_admin):
        return ((1, 'Yes'), (0, 'No'))

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(completed=True if int(self.value()) == 1 else False)
        return queryset


#########################
# Admins
#########################

# admin action - export Entry as csv
def export_in_browser(modeladmin, request, queryset):
    return HttpResponseRedirect(request.build_absolute_uri(
        '%s?%s' % (reverse('export_entries_browser'), urllib.urlencode({'id': [e.id for e in queryset]}, True))))
export_in_browser.short_description = "Export as .csv (in browser)"

def export_as_csv(modeladmin, request, queryset):
    return HttpResponseRedirect(request.build_absolute_uri(
        '%s?%s' % (reverse('export_entries'), urllib.urlencode({'id': [e.id for e in queryset]}, True))))
export_as_csv.short_description = "Export as .csv"


class EntryAdmin(admin.ModelAdmin):
    list_filter = (RouteListFilter, SurveyListFilter, AuditorListFilter, CompletedListFilter)
    search_fields = ['route_number', 'auditor__username']
    list_display = ('route_number', 'survey', 'auditor', 'completed',
                    'start_time', 'end_time', 'submitted', 'starting_address', 'ending_address')
    # expands the filter sidebar so you can see each filter
    change_list_template = "admin/change_list_filter_sidebar.html"
    actions = (export_in_browser, export_as_csv)
    ordering = ['-submitted']

    # don't allow editing the survey type when it's an existing entry
    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ('survey',)
        else:
            return super(EntryAdmin, self).get_readonly_fields(request, obj)

#########################
# Register models
#########################

# Entry
admin.site.register(Entry, EntryAdmin)
