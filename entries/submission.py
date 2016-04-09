import json
from datetime import datetime
from django.db import IntegrityError
from django.utils import timezone
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from entries.models import *


class Submit(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(Submit, self).dispatch(request, *args, **kwargs)

    def post(self, request):

        # not logged in
        if not request.user.is_authenticated():
            return HttpResponse(json.dumps({
                'success': False,
                'errorCode': 'not-logged-in',
                'errorMessage': 'Your session has expired.'
            }), content_type="application/json")

        route = json.loads(request.body)

        if route:

            # log for debugging purposes
            log = EntryLog(
                route_id=route.get('id'),
                survey_id=route.get('survey_id'),
                json=request.body,
            )
            log.save()

            # parse the start and end time (and add tz) in the following possible formats:
            # 2014-12-01T14:00
            # 2014-12-01T14:00:00
            # 2014-12-01T14:00:00.000
            try:

                start_time = None
                end_time = None

                if route.get('start_time'):
                    start_time = datetime.fromtimestamp(int(route.get('start_time')))
                    start_time = timezone.make_aware(start_time, timezone.get_default_timezone())

                # we shouldn't have an end time until it's fully complete
                if route.get('end_time') and route.get('completed'):
                    end_time = datetime.fromtimestamp(int(route.get('end_time')))
                    end_time = timezone.make_aware(end_time, timezone.get_default_timezone())

            # couldn't parse dates so log error and default times to now
            except Exception as e:
                log.entrylogmessage_set.create(message='Invalid start/end dates (%s)' % e)
                start_time = timezone.now()
                end_time = timezone.now()

            try:
                entry_submission = Entry(
                    survey_id=route.get('survey_id'),
                    auditor=request.user,
                    route_number=route.get('id'),
                    start_time=start_time,
                    end_time=end_time,
                    completed=route.get('completed', False),
                    starting_address=route.get('starting_address'),
                    ending_address=route.get('ending_address'),
                    submitted=timezone.now(),
                )
                entry_submission.save()

                sections = route.get('sections')

                for index, section in enumerate(sections):

                    try:

                        section_form = section.get('form', {})
                        section_item_entries = section.get('entries')
                        coords = section.get('coords', {})

                        if section.get('name') == 'route':

                            # save the route section
                            entry_section = EntryRouteSection(
                                entry=entry_submission,
                                position=index,
                            )
                            entry_section.save()

                            self.save_entries(
                                entry_section, section_item_entries,
                                EntryRouteItemOption, EntryRouteSubItemOption,
                                EntryRouteItemAuxiliary, EntryRouteSubItemAuxiliary,
                                EntryRouteItemNA, EntryRouteSubItemNA)

                        elif section.get('name') == 'segment':

                            # save the segment section
                            entry_section = EntrySegmentSection(
                                entry=entry_submission,
                                position=index,
                                segment_id=section_form.get('id'),
                                street=section_form.get('street'),
                                side=section_form.get('side'),
                                starting_xstreet=section_form.get('starting_xstreet'),
                                ending_xstreet=section_form.get('ending_xstreet'),
                                latitude=coords.get('latitude', None),
                                longitude=coords.get('longitude', None)
                            )
                            entry_section.save()

                            self.save_entries(
                                entry_section, section_item_entries,
                                EntrySegmentItemOption, EntrySegmentSubItemOption,
                                EntrySegmentItemAuxiliary, EntrySegmentSubItemAuxiliary,
                                EntrySegmentItemNA, EntrySegmentSubItemNA)

                        elif section.get('name') == 'crossing':

                            # save the crossing section
                            entry_section = EntryCrossingSection(
                                entry=entry_submission,
                                position=index,
                                crossing_id=section_form.get('id'),
                                crossing_from=section_form.get('crossing_from'),
                                crossing_to=section_form.get('crossing_to'),
                                intersection1=section_form.get('intersection1'),
                                intersection2=section_form.get('intersection2'),
                                latitude=coords.get('latitude', None),
                                longitude=coords.get('longitude', None)
                            )
                            entry_section.save()

                            self.save_entries(
                                entry_section, section_item_entries,
                                EntryCrossingItemOption, EntryCrossingSubItemOption,
                                EntryCrossingItemAuxiliary, EntryCrossingSubItemAuxiliary,
                                EntryCrossingItemNA, EntryCrossingSubItemNA)

                        elif section.get('name') == 'culdesac':

                            # save the culdesac section
                            entry_section = EntryCuldesacSection(
                                entry=entry_submission,
                                position=index,
                                culdesac_id=section_form.get('id'),
                                street=section_form.get('street'),
                                latitude=coords.get('latitude', None),
                                longitude=coords.get('longitude', None)
                            )
                            entry_section.save()

                            self.save_entries(
                                entry_section, section_item_entries,
                                EntryCuldesacItemOption, EntryCuldesacSubItemOption,
                                EntryCuldesacItemAuxiliary, EntryCuldesacSubItemAuxiliary,
                                EntryCuldesacItemNA, EntryCuldesacSubItemNA)

                    # skip any database integrity errors because... what can we do?
                    except IntegrityError as e:
                        msg = 'Integrity Error (skipping): %s' % e
                        print msg
                        log.entrylogmessage_set.create(message=msg)
                        continue

            except Exception as e:
                print 'Exception: %s' % e
                log.entrylogmessage_set.create(message=e)
                raise e

        return HttpResponse(json.dumps({'success': True}), content_type="application/json")

    def save_entries(self, entry_section, entries, item_option, sub_item_option, item_aux, sub_item_aux, item_na, sub_item_na):
        """
        :type entry_section: EntrySection
        :type entries: list
        :type item_option: entries.models.EntryItemOption
        :type sub_item_option: entries.models.EntryItemOption
        :type item_aux: entries.models.EntryItemAuxiliary
        :type sub_item_aux: entries.models.EntryItemAuxiliary
        :type item_na: entries.models.EntryItemNA
        :type sub_item_na: entries.models.EntrySubItemNA
        """

        for entry in entries:

            # sub item
            if entry.get('is_sub_item') == '1':
                # auxiliary input (text/number)
                if entry.get('item_type') in ['text', 'number']:
                    sub_item_aux(
                        item_id=entry.get('item_id'),
                        section_id=entry_section.id,
                        value=entry.get('value')
                    ).save()
                # Not applicable
                elif entry.get('value') == NOT_APPLICABLE:
                    sub_item_na(
                        item_id=entry.get('item_id'),
                        section_id=entry_section.id,
                    ).save()
                # item option
                else:
                    sub_item_option(
                        section_id=entry_section.id,
                        option_id=entry.get('value'),
                    ).save()
            # regular item
            else:
                # auxiliary input (text/number)
                if entry.get('item_type') in ['text', 'number']:
                    item_aux(
                        item_id=entry.get('item_id'),
                        section_id=entry_section.id,
                        value=entry.get('value')
                    ).save()
                # Not applicable
                elif entry.get('value') == NOT_APPLICABLE:
                    item_na(
                        item_id=entry.get('item_id'),
                        section_id=entry_section.id,
                    ).save()
                # item option
                else:
                    item_option(
                        section_id=entry_section.id,
                        option_id=entry.get('value'),
                    ).save()


class Retrieve(View):

    def dispatch(self, request, *args, **kwargs):
        return super(Retrieve, self).dispatch(request, *args, **kwargs)

    def get(self, request):

        # not logged in
        if not request.user.is_authenticated():
            return HttpResponse(json.dumps({
                'success': False,
                'errorCode': 'not-logged-in',
                'errorMessage': 'Your session has expired.'
            }), content_type="application/json")

        entries = []
        unique_route_entries = {}

        # get incomplete entry submissions and unique by route number
        user_entries = Entry.objects.filter(completed=False, auditor=request.user).order_by('-submitted')
        for entry in user_entries:
            if entry.route_number not in unique_route_entries.keys():
                unique_route_entries[entry.route_number] = entry

        # filter out routes that also have a completed entry submission
        completed_route_entries = Entry.objects.filter(route_number__in=unique_route_entries.keys(), completed=True)

        for entry in completed_route_entries:
            if entry.route_number in unique_route_entries.keys():
                del unique_route_entries[entry.route_number]

        for route_number, entry in unique_route_entries.items():

            sections = []

            # Route section - include this section if the survey has route items, regardless if there's any entries
            if entry.survey.routeitem_set.exists():
                sections.append({
                    'name': 'route',
                    'position': 0,  # the roue is always the first section
                    'entries': self.get_entry_items(
                        entry.entryroutesection_set.all()[0] if entry.entryroutesection_set.exists() else None,
                        EntryRouteItemOption, EntryRouteSubItemOption,
                        EntryRouteItemAuxiliary, EntryRouteSubItemAuxiliary,
                        EntryRouteItemNA, EntryRouteSubItemNA)
                })

            # Segment sections
            segment_sections = entry.entrysegmentsection_set.order_by('id')
            if segment_sections.exists():
                for segment_section in segment_sections:
                    sections.append({
                        'name': segment_section.name,
                        'position': segment_section.position,
                        'form': {
                            'id': segment_section.segment_id,
                            'street': segment_section.street,
                            'side': segment_section.side,
                            'starting_xstreet': segment_section.starting_xstreet,
                            'ending_xstreet': segment_section.ending_xstreet,
                        },
                        'coords': {'latitude': segment_section.latitude, 'longitude': segment_section.longitude},
                        'entries': self.get_entry_items(
                            segment_section,
                            EntrySegmentItemOption, EntrySegmentSubItemOption,
                            EntrySegmentItemAuxiliary, EntrySegmentSubItemAuxiliary,
                            EntrySegmentItemNA, EntrySegmentSubItemNA)
                    })

            # Crossing sections
            crossing_sections = entry.entrycrossingsection_set.order_by('id')
            if crossing_sections.exists():
                for crossing_section in crossing_sections:
                    sections.append({
                        'name': crossing_section.name,
                        'position': crossing_section.position,
                        'form': {
                            'id': crossing_section.crossing_id,
                            'crossing_from': crossing_section.crossing_from,
                             'crossing_to': crossing_section.crossing_to,
                            'intersection1': crossing_section.intersection1,
                            'intersection2': crossing_section.intersection2,
                        },
                        'coords': {'latitude': crossing_section.latitude, 'longitude': crossing_section.longitude},
                        'entries': self.get_entry_items(
                            crossing_section,
                            EntryCrossingItemOption, EntryCrossingSubItemOption,
                            EntryCrossingItemAuxiliary, EntryCrossingSubItemAuxiliary,
                            EntryCrossingItemNA, EntryCrossingSubItemNA)
                    })

            # Culdesac sections
            culdesac_sections = entry.entryculdesacsection_set.order_by('id')
            if culdesac_sections.exists():
                for culdesac_section in culdesac_sections:
                    sections.append({
                        'name': culdesac_section.name,
                        'position': culdesac_section.position,
                        'form': {
                            'id': culdesac_section.culdesac_id,
                            'street': culdesac_section.street,
                        },
                        'coords': {'latitude': culdesac_section.latitude, 'longitude': culdesac_section.longitude},
                        'entries': self.get_entry_items(
                            culdesac_section,
                            EntryCuldesacItemOption, EntryCuldesacSubItemOption,
                            EntryCuldesacItemAuxiliary, EntryCuldesacSubItemAuxiliary,
                            EntryCuldesacItemNA, EntryCuldesacSubItemNA)
                    })

            # survey type "mini segment" needs exactly a crossing, then a segment, then a final crossing, in that order
            # if no entries exist so far for these sections, then go ahead and create them on the fly for the UI
            if entry.survey.type and entry.survey.type.slug == 'mini_segment' and not segment_sections.exists() and not crossing_sections.exists():
                sections.append({'name': 'crossing', 'position': 0, 'form': {}, 'entries': []})
                sections.append({'name': 'segment', 'position': 1, 'form': {}, 'entries': []})
                sections.append({'name': 'crossing', 'position': 2, 'form': {}, 'entries': []})

            # sort by section position
            sections = sorted(sections, key=lambda section: section['position'])

            returned_entry = {
                'id': entry.route_number,
                'survey_id': entry.survey.id,
                'starting_address': entry.starting_address,
                'ending_address': entry.ending_address,
                'sections': sections,
                'synced': True,
                'username': request.user.username,
            }

            # add in start/end times if they exist
            if entry.start_time:
                returned_entry.update({'start_time': timezone.localtime(entry.start_time).strftime('%s')})
            if entry.end_time:
                returned_entry.update({'end_time': timezone.localtime(entry.end_time).strftime('%s')})

            entries.append(returned_entry)

        return HttpResponse(json.dumps(entries), content_type="application/json")

    def get_entry_items(self, entry_section, item_option, sub_item_option, item_aux, sub_item_aux, item_na, sub_item_na):
        """
        :rtype : list
        :type entry_section: entries.models.EntrySection
        :type item_option: entries.models.EntryItemOption
        :type sub_item_option: entries.models.EntryItemOption
        :type item_aux: entries.models.EntryItemAuxiliary
        :type sub_item_aux: entries.models.EntryItemAuxiliary
        :type item_na: entries.models.EntryItemNA
        :type sub_item_na: entries.models.EntrySubItemNA
        """

        entries = []

        # item options
        for option in item_option.objects.filter(section=entry_section):
            try:
                entries.append({
                    'is_sub_item': '0',
                    'item_id': option.option.item.id,
                    'item_type': option.option.item.type,
                    'route_id': entry_section.entry.route_number,
                    'survey_section': entry_section.name,
                    'value': option.option.id,
                })
            except:
                continue

        # sub item options
        for option in sub_item_option.objects.filter(section=entry_section):
            try:
                entries.append({
                    'is_sub_item': '1',
                    'item_id': option.option.item.id,
                    'item_type': option.option.item.type,
                    'route_id': entry_section.entry.route_number,
                    'survey_section': entry_section.name,
                    'value': option.option.id,
                })
            except:
                continue

        # item auxiliaries
        for aux in item_aux.objects.filter(section=entry_section):
            try:
                entries.append({
                    'is_sub_item': '0',
                    'item_id': aux.item.id,
                    'item_type': aux.item.type,
                    'route_id': entry_section.entry.route_number,
                    'survey_section': entry_section.name,
                    'value': aux.value,
                })
            except:
                continue

        # sub item auxiliaries
        for aux in sub_item_aux.objects.filter(section=entry_section):
            try:
                entries.append({
                    'is_sub_item': '1',
                    'item_id': aux.item.id,
                    'item_type': aux.item.type,
                    'route_id': entry_section.entry.route_number,
                    'survey_section': entry_section.name,
                    'value': aux.value,
                })
            except:
                continue

        # not applicable item
        for na in item_na.objects.filter(section=entry_section):
            try:
                entries.append({
                    'is_sub_item': '0',
                    'item_id': na.item.id,
                    'item_type': na.item.type,
                    'route_id': entry_section.entry.route_number,
                    'survey_section': entry_section.name,
                    'value': NOT_APPLICABLE,
                })
            except:
                continue

        # not applicable sub item
        for na in sub_item_na.objects.filter(section=entry_section):
            try:
                entries.append({
                    'is_sub_item': 1,
                    'item_id': na.item.id,
                    'item_type': na.item.type,
                    'route_id': entry_section.entry.route_number,
                    'survey_section': entry_section.name,
                    'value': NOT_APPLICABLE,
                })
            except:
                continue

        return entries
