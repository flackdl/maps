from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from maps.models import *


NOT_APPLICABLE = '-777'


class EntryLog(models.Model):
    """
    for debugging submissions
    """
    route_id = models.CharField(max_length=255, null=True)
    survey_id = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(default=timezone.now)
    json = models.TextField(null=True)


class EntryLogMessage(models.Model):
    """
    for debugging submissions - messages
    """
    entry_log = models.ForeignKey(EntryLog)
    message = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return '%s (%s)' % (self.message, self.entry_log.id)


# ####################################################################3


class Entry(models.Model):
    survey = models.ForeignKey(Survey)
    auditor = models.ForeignKey(User)
    route_number = models.CharField(max_length=255)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    submitted = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    starting_address = models.CharField(max_length=255, null=True, blank=True)
    ending_address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('submitted',)  # order by most recent submission
        verbose_name_plural = "entries"

    def __unicode__(self):
        return '#%s : %s' % (self.route_number, self.auditor)


class EntrySection(models.Model):
    entry = models.ForeignKey(Entry)
    position = models.PositiveSmallIntegerField(default=0)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class EntryItemOption(models.Model):
    def __unicode__(self):
        return '%s : %s' % (self.option.item, self.option)

    class Meta:
        abstract = True


class EntryItemAuxiliary(models.Model):
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s : %s' % (self.item, self.value)

    class Meta:
        abstract = True


class EntryItemNA(models.Model):
    def __unicode__(self):
        return self.item

    class Meta:
        abstract = True


class EntrySubItemNA(models.Model):
    def __unicode__(self):
        return self.item

    class Meta:
        abstract = True


##########################
# Route
##########################

# route section


class EntryRouteSection(EntrySection):
    name = 'route'


# route item

class EntryRouteItemOption(EntryItemOption):
    section = models.ForeignKey(EntryRouteSection)
    option = models.ForeignKey(RouteItemOption)


# route sub item


class EntryRouteSubItemOption(EntryItemOption):
    section = models.ForeignKey(EntryRouteSection)
    option = models.ForeignKey(RouteSubItemOption)


# route item aux


class EntryRouteItemAuxiliary(EntryItemAuxiliary):
    section = models.ForeignKey(EntryRouteSection)
    item = models.ForeignKey(RouteItem)


# route sub item aux


class EntryRouteSubItemAuxiliary(EntryItemAuxiliary):
    section = models.ForeignKey(EntryRouteSection)
    item = models.ForeignKey(RouteSubItem)


class EntryRouteItemNA(EntryItemNA):
    section = models.ForeignKey(EntryRouteSection)
    item = models.ForeignKey(RouteItem)


class EntryRouteSubItemNA(EntrySubItemNA):
    section = models.ForeignKey(EntryRouteSection)
    item = models.ForeignKey(RouteSubItem)


##########################
# Segment
##########################

# segment section


class EntrySegmentSection(EntrySection):
    segment_id = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, null=True)
    side = models.CharField(max_length=255, null=True)
    starting_xstreet = models.CharField(max_length=255, null=True)
    ending_xstreet = models.CharField(max_length=255, null=True)

    name = 'segment'


# segment item


class EntrySegmentItemOption(EntryItemOption):
    section = models.ForeignKey(EntrySegmentSection)
    option = models.ForeignKey(SegmentItemOption)


# segment sub item


class EntrySegmentSubItemOption(EntryItemOption):
    section = models.ForeignKey(EntrySegmentSection)
    option = models.ForeignKey(SegmentSubItemOption)


# segment item aux

class EntrySegmentItemAuxiliary(EntryItemAuxiliary):
    section = models.ForeignKey(EntrySegmentSection)
    item = models.ForeignKey(SegmentItem)


# segment sub item aux


class EntrySegmentSubItemAuxiliary(EntryItemAuxiliary):
    section = models.ForeignKey(EntrySegmentSection)
    item = models.ForeignKey(SegmentSubItem)


class EntrySegmentItemNA(EntryItemNA):
    section = models.ForeignKey(EntrySegmentSection)
    item = models.ForeignKey(SegmentItem)


class EntrySegmentSubItemNA(EntrySubItemNA):
    section = models.ForeignKey(EntrySegmentSection)
    item = models.ForeignKey(SegmentSubItem)


##########################
# Crossing
##########################

# crossing section


class EntryCrossingSection(EntrySection):
    crossing_id = models.CharField(max_length=255, null=True)
    crossing_from = models.CharField(max_length=255, null=True)
    crossing_to = models.CharField(max_length=255, null=True)
    intersection1 = models.CharField(max_length=255, null=True)
    intersection2 = models.CharField(max_length=255, null=True)

    name = 'crossing'


# crossing item


class EntryCrossingItemOption(EntryItemOption):
    section = models.ForeignKey(EntryCrossingSection)
    option = models.ForeignKey(CrossingItemOption)


# crossing sub item


class EntryCrossingSubItemOption(EntryItemOption):
    section = models.ForeignKey(EntryCrossingSection)
    option = models.ForeignKey(CrossingSubItemOption)


# crossing item aux


class EntryCrossingItemAuxiliary(EntryItemAuxiliary):
    section = models.ForeignKey(EntryCrossingSection)
    item = models.ForeignKey(CrossingItem)


# crossing sub item aux


class EntryCrossingSubItemAuxiliary(EntryItemAuxiliary):
    section = models.ForeignKey(EntryCrossingSection)
    item = models.ForeignKey(CrossingSubItem)


class EntryCrossingItemNA(EntryItemNA):
    section = models.ForeignKey(EntryCrossingSection)
    item = models.ForeignKey(CrossingItem)


class EntryCrossingSubItemNA(EntrySubItemNA):
    section = models.ForeignKey(EntryCrossingSection)
    item = models.ForeignKey(CrossingSubItem)


##########################
# Culdesac
##########################

# culdesac section


class EntryCuldesacSection(EntrySection):
    culdesac_id = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, null=True)

    name = 'culdesac'


# culdesac item


class EntryCuldesacItemOption(EntryItemOption):
    section = models.ForeignKey(EntryCuldesacSection)
    option = models.ForeignKey(CuldesacItemOption)


# culdesac sub item


class EntryCuldesacSubItemOption(EntryItemOption):
    section = models.ForeignKey(EntryCuldesacSection)
    option = models.ForeignKey(CuldesacSubItemOption)


# culdesac item aux


class EntryCuldesacItemAuxiliary(EntryItemAuxiliary):
    section = models.ForeignKey(EntryCuldesacSection)
    item = models.ForeignKey(CuldesacItem)


# culdesac sub item aux


class EntryCuldesacSubItemAuxiliary(EntryItemAuxiliary):
    section = models.ForeignKey(EntryCuldesacSection)
    item = models.ForeignKey(CuldesacSubItem)


class EntryCuldesacItemNA(EntryItemNA):
    section = models.ForeignKey(EntryCrossingSection)
    item = models.ForeignKey(CuldesacItem)


class EntryCuldesacSubItemNA(EntrySubItemNA):
    section = models.ForeignKey(EntryCrossingSection)
    item = models.ForeignKey(CuldesacSubItem)
