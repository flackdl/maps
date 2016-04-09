from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from maps.models import Survey, RouteItemHelper, CodePrefix
from maps.models import SELECT, SELECT_MULTIPLE
from maps.models import RouteSubItemHelper, SegmentSubItemHelper, CrossingSubItemHelper
from maps.models import SegmentItemHelper, CrossingItemHelper
from maps.models import RouteItem, SegmentItem, CrossingItem
from maps.models import RouteSubItem, SegmentSubItem, CrossingSubItem
from maps.models import RouteItemOption, SegmentItemOption, CrossingItemOption
from maps.models import RouteSubItemOption, SegmentSubItemOption, CrossingSubItemOption
from maps.models import CuldesacItem, CuldesacItemHelper, CuldesacItemOption, CuldesacSubItem, CuldesacSubItemHelper, CuldesacSubItemOption
from maps.models import SUB_ITEM


#####################################################
# Inlines
#####################################################

class EditInline():
    extra = 1
    readonly_fields = ['edit']


class SubItemInline():
    extra = 1
    readonly_fields = ['edit']


# items

class SortableInline():
    sortable_field_name = "position"


class RouteItemInline(SortableInline, EditInline, admin.TabularInline):
    model = RouteItem


class RouteSubItemInline(SortableInline, SubItemInline, admin.TabularInline):
    model = RouteSubItem
    fk_name = 'item'


class SegmentItemInline(SortableInline, EditInline, admin.TabularInline):
    model = SegmentItem


class SegmentSubItemInline(SortableInline, SubItemInline, admin.TabularInline):
    model = SegmentSubItem
    fk_name = 'item'


class CrossingItemInline(SortableInline, EditInline, admin.TabularInline):
    model = CrossingItem


class CrossingSubItemInline(SortableInline, SubItemInline, admin.TabularInline):
    model = CrossingSubItem
    fk_name = 'item'


class CuldesacItemInline(SortableInline, EditInline, admin.TabularInline):
    model = CuldesacItem


class CuldesacSubItemInline(SortableInline, SubItemInline, admin.TabularInline):
    model = CuldesacSubItem
    fk_name = 'item'


# item options


class RouteItemOptionInline(admin.TabularInline):
    extra = 1
    model = RouteItemOption


class RouteSubItemOptionInline(admin.TabularInline):
    extra = 1
    model = RouteSubItemOption


class SegmentItemOptionInline(admin.TabularInline):
    extra = 1
    model = SegmentItemOption


class SegmentSubItemOptionInline(admin.TabularInline):
    extra = 1
    model = SegmentSubItemOption


class CrossingItemOptionInline(admin.TabularInline):
    extra = 1
    model = CrossingItemOption


class CrossingSubItemOptionInline(admin.TabularInline):
    extra = 1
    model = CrossingSubItemOption


class CuldesacItemOptionInline(admin.TabularInline):
    extra = 1
    model = CuldesacItemOption


class CuldesacSubItemOptionInline(admin.TabularInline):
    extra = 1
    model = CuldesacSubItemOption


# Item Helpers
class ItemHelper():
    extra = 1
    max_num = 1


class RouteItemHelperInline(ItemHelper, admin.TabularInline):
    model = RouteItemHelper


class RouteSubItemHelperInline(ItemHelper, admin.TabularInline):
    model = RouteSubItemHelper


class SegmentItemHelperInline(ItemHelper, admin.TabularInline):
    model = SegmentItemHelper


class SegmentSubItemHelperInline(ItemHelper, admin.TabularInline):
    model = SegmentSubItemHelper


class CrossingItemHelperInline(ItemHelper, admin.TabularInline):
    model = CrossingItemHelper


class CrossingSubItemHelperInline(ItemHelper, admin.TabularInline):
    model = CrossingSubItemHelper


class CuldesacItemHelperInline(ItemHelper, admin.TabularInline):
    model = CuldesacItemHelper


class CuldesacSubItemHelperInline(ItemHelper, admin.TabularInline):
    model = CuldesacSubItemHelper


#####################################################
# Admins
#####################################################


# inherit this for models you don't want listed
class HideFromAdmin():
    get_model_perms = lambda self, req: {}


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('version', 'published')

    inlines = [
        RouteItemInline,
        SegmentItemInline,
        CrossingItemInline,
        CuldesacItemInline,
    ]

    # redirect the user to the actual survey admin after saving
    def response_change(self, request, obj, post_url_continue=None):
        # return user to the same survey if they just hit save
        if "_continue" not in request.POST and '_addanother' not in request.POST:
            return HttpResponseRedirect(reverse("admin:maps_survey_change", args=[obj.id]))
        return super(SurveyAdmin, self).response_change(request, obj)

# items


class ItemAdmin(admin.ModelAdmin):

    class Media:
        js = [
            "grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js",
            "js/tinymce_setup.js",
        ]

    # enforce "type" as a readonly field so we can override the get_inline_instances to dynamically adjust which
    # inlines are provided. Otherwise, there's issues with the admin management data being wrong after update
    readonly_fields = ['type']

    _default_not_implemented_message = 'Extending class needs to implement this'

    def __init__(self, *args, **kwargs):
        super(ItemAdmin, self).__init__(*args, **kwargs)

    # redirect the user to the actual survey admin after saving
    def response_change(self, request, obj, post_url_continue=None):
        if "_continue" not in request.POST and '_addanother' not in request.POST:
            return HttpResponseRedirect(reverse("admin:maps_survey_change", args=[obj.survey.id]))
        return super(ItemAdmin, self).response_change(request, obj)

    def _item_option_inline(self):
        raise NotImplementedError(self._default_not_implemented_message)

    def _sub_item_inline(self):
        raise NotImplementedError(self._default_not_implemented_message)

    def _item_helper_inline(self):
        raise NotImplementedError(self._default_not_implemented_message)

    def get_inline_instances(self, request, obj=None):

        inlines = []

        # item option inline
        if obj and obj.type in [SELECT, SELECT_MULTIPLE]:
            inlines.append(self._item_option_inline())
        # sub item inline
        elif obj and obj.type == SUB_ITEM:
            inlines.append(self._sub_item_inline())

        # item helper
        inlines.append(self._item_helper_inline())

        return inlines


class SubItemAdmin(ItemAdmin):

    readonly_fields = ['type', 'item', 'position']

    # redirect the user to the actual survey admin after saving
    def response_change(self, request, obj, post_url_continue=None):
        if "_continue" not in request.POST:
            return HttpResponseRedirect(reverse("admin:maps_survey_change", args=[obj.item.survey.id]))
        return super(SubItemAdmin, self).response_change(request, obj)

    # sub items shouldn't have more sub items (right?)
    def _sub_item_inline(self):
        return []


class RouteItemAdmin(ItemAdmin):

    def _item_option_inline(self):
        return RouteItemOptionInline(self.model, self.admin_site)

    def _sub_item_inline(self):
        return RouteSubItemInline(self.model, self.admin_site)

    def _item_helper_inline(self):
        return RouteItemHelperInline(self.model, self.admin_site)


class SegmentItemAdmin(ItemAdmin):

    def _item_option_inline(self):
        return SegmentItemOptionInline(self.model, self.admin_site)

    def _sub_item_inline(self):
        return SegmentSubItemInline(self.model, self.admin_site)

    def _item_helper_inline(self):
        return SegmentItemHelperInline(self.model, self.admin_site)


class CrossingItemAdmin(ItemAdmin):

    def _item_option_inline(self):
        return CrossingItemOptionInline(self.model, self.admin_site)

    def _sub_item_inline(self):
        return CrossingSubItemInline(self.model, self.admin_site)

    def _item_helper_inline(self):
        return CrossingItemHelperInline(self.model, self.admin_site)


class CuldesacItemAdmin(ItemAdmin):

    def _item_option_inline(self):
        return CuldesacItemOptionInline(self.model, self.admin_site)

    def _sub_item_inline(self):
        return CuldesacSubItemInline(self.model, self.admin_site)

    def _item_helper_inline(self):
        return CuldesacItemHelperInline(self.model, self.admin_site)


# sub-items


class RouteSubItemAdmin(SubItemAdmin):

    def _item_option_inline(self):
        return RouteSubItemOptionInline(self.model, self.admin_site)

    def _item_helper_inline(self):
        return RouteSubItemHelperInline(self.model, self.admin_site)


class SegmentSubItemAdmin(SubItemAdmin):

    def _item_option_inline(self):
        return SegmentSubItemOptionInline(self.model, self.admin_site)

    def _item_helper_inline(self):
        return SegmentSubItemHelperInline(self.model, self.admin_site)


class CrossingSubItemAdmin(SubItemAdmin):

    def _item_option_inline(self):
        return CrossingSubItemOptionInline(self.model, self.admin_site)

    def _item_helper_inline(self):
        return CrossingSubItemHelperInline(self.model, self.admin_site)


class CuldesacSubItemAdmin(SubItemAdmin):

    def _item_option_inline(self):
        return CuldesacSubItemOptionInline(self.model, self.admin_site)

    def _item_helper_inline(self):
        return CuldesacSubItemHelperInline(self.model, self.admin_site)


# Survey parts
admin.site.register(Survey, SurveyAdmin)

# Code prefix
admin.site.register(CodePrefix)

# Items / Sub-Items
admin.site.register(RouteItem, RouteItemAdmin)
admin.site.register(SegmentItem, SegmentItemAdmin)
admin.site.register(CrossingItem, CrossingItemAdmin)
admin.site.register(CuldesacItem, CuldesacItemAdmin)

admin.site.register(RouteSubItem, RouteSubItemAdmin)
admin.site.register(SegmentSubItem, SegmentSubItemAdmin)
admin.site.register(CrossingSubItem, CrossingSubItemAdmin)
admin.site.register(CuldesacSubItem, CuldesacSubItemAdmin)

# Item Options
admin.site.register(RouteItemOption)
admin.site.register(SegmentItemOption)
admin.site.register(CrossingItemOption)
admin.site.register(CuldesacItemOption)

# Helpers
admin.site.register(RouteItemHelper)
admin.site.register(RouteSubItemHelper)
admin.site.register(SegmentItemHelper)
admin.site.register(SegmentSubItemHelper)
admin.site.register(CrossingItemHelper)
admin.site.register(CrossingSubItemHelper)
admin.site.register(CuldesacItemHelper)
admin.site.register(CuldesacSubItemHelper)
