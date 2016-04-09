from django.core.urlresolvers import reverse
from django.db import models
from django.utils.safestring import mark_safe


###########################################
# Survey
###########################################


class AdminEdit(models.Model):

    class Meta:
        abstract = True

    def edit(self):

        if self.id:
            return mark_safe('<a href="%s">Edit</a>' % (
                reverse('admin:%s_change' % self._meta.db_table, args=[self.id])))
        else:
            return ''


class SurveyType(models.Model):
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.slug


class Survey(models.Model):
    version = models.CharField(max_length=255, unique=True)
    published = models.BooleanField(default=False, help_text='Whether this survey is visible to users or not')
    type = models.ForeignKey(SurveyType, null=True, blank=True, verbose_name='Survey Type',
                             help_text='Certain surveys have specific rules. Leave blank for default behavior')

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return self.version


class CodePrefix(models.Model):
    prefix = models.CharField(max_length=255)

    def __unicode__(self):
        return self.prefix


########################################
# Items
########################################

TEXT = 'text'
SELECT = 'select'
SELECT_MULTIPLE = 'select-multiple'
INTEGER = 'number'
SUB_ITEM = 'sub-items'

QUESTION_TYPES = (
    (TEXT, 'Text'),
    (INTEGER, 'Integer'),
    (SELECT, 'Select'),
    (SELECT_MULTIPLE, 'Select Multiple'),
    (SUB_ITEM, 'Sub Items'),
)


class Item(models.Model):
    title = models.TextField()
    code_prefix = models.ForeignKey(CodePrefix)
    type = models.CharField(max_length=255, choices=QUESTION_TYPES)
    include_not_applicable = models.BooleanField(default=False)
    position = models.PositiveSmallIntegerField(
        "Position", help_text='Numerical position for Item.  Leave empty for default')

    class Meta:
        abstract = True
        ordering = ['position']

    def __unicode__(self):
        return self.title


class RouteItem(Item, AdminEdit):
    survey = models.ForeignKey(Survey)


class RouteSubItem(Item, AdminEdit):
    item = models.ForeignKey(RouteItem, related_name='subitem_set')


class SegmentItem(Item, AdminEdit):
    survey = models.ForeignKey(Survey)


class SegmentSubItem(Item, AdminEdit):
    item = models.ForeignKey(SegmentItem, related_name='subitem_set')


class CrossingItem(Item, AdminEdit):
    survey = models.ForeignKey(Survey)


class CrossingSubItem(Item, AdminEdit):
    item = models.ForeignKey(CrossingItem, related_name='subitem_set')


class CuldesacItem(Item, AdminEdit):
    survey = models.ForeignKey(Survey)


class CuldesacSubItem(Item, AdminEdit):
    item = models.ForeignKey(CuldesacItem, related_name='subitem_set')


########################################
# Item options
########################################

class ItemOption(models.Model):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class RouteItemOption(ItemOption):
    item = models.ForeignKey(RouteItem, related_name='itemoption_set')


class RouteSubItemOption(ItemOption):
    item = models.ForeignKey(RouteSubItem, related_name='itemoption_set')


class SegmentItemOption(ItemOption):
    item = models.ForeignKey(SegmentItem, related_name='itemoption_set')


class SegmentSubItemOption(ItemOption):
    item = models.ForeignKey(SegmentSubItem, related_name='itemoption_set')


class CrossingItemOption(ItemOption):
    item = models.ForeignKey(CrossingItem, related_name='itemoption_set')


class CrossingSubItemOption(ItemOption):
    item = models.ForeignKey(CrossingSubItem, related_name='itemoption_set')


class CuldesacItemOption(ItemOption):
    item = models.ForeignKey(CuldesacItem, related_name='itemoption_set')


class CuldesacSubItemOption(ItemOption):
    item = models.ForeignKey(CuldesacSubItem, related_name='itemoption_set')


########################################
# Item Helper/Pop-ups
########################################

class ItemHelper(models.Model):
    #content = tinymce_models.HTMLField()
    content = models.TextField()

    class Meta:
        abstract = True


class RouteItemHelper(ItemHelper):
    item = models.ForeignKey(RouteItem, related_name='itemhelper_set')


class RouteSubItemHelper(ItemHelper):
    item = models.ForeignKey(RouteSubItem, related_name='itemhelper_set')


class SegmentItemHelper(ItemHelper):
    item = models.ForeignKey(SegmentItem, related_name='itemhelper_set')


class SegmentSubItemHelper(ItemHelper):
    item = models.ForeignKey(SegmentSubItem, related_name='itemhelper_set')


class CrossingItemHelper(ItemHelper):
    item = models.ForeignKey(CrossingItem, related_name='itemhelper_set')


class CrossingSubItemHelper(ItemHelper):
    item = models.ForeignKey(CrossingSubItem, related_name='itemhelper_set')


class CuldesacItemHelper(ItemHelper):
    item = models.ForeignKey(CuldesacItem, related_name='itemhelper_set')


class CuldesacSubItemHelper(ItemHelper):
    item = models.ForeignKey(CuldesacSubItem, related_name='itemhelper_set')

