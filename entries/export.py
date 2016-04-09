import csv
from django.http import HttpResponse
from maps.models import *
from entries.models import *
from django.shortcuts import render
from django.views.generic import View
from entries.utils import *


ALPHABET = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u' 'v', 'w', 'x', 'y', 'z')


class Export(View):

    render_in_browser = False

    def get(self, request):

        ids = request.GET.getlist('id')
        entries = Entry.objects.filter(id__in=[int(i) for i in ids]).order_by('submitted')

        # verify the entries are for the same survey type
        if len(set([entry.survey.id for entry in entries])) > 1:
            return render(request, 'entries/export.html', {
                'error': 'Entries of different survey types cannot be exported simultaneously'})

        rows = []

        for entry in entries:

            cols = [
                {
                    'col': 'Route ID',
                    'val': entry.route_number,
                },
                {
                    'col': 'address_starting',
                    'val': entry.starting_address if entry.starting_address else '',
                },
                {
                    'col': 'address_ending',
                    'val': entry.ending_address if entry.starting_address else '',
                },
                {
                    'col': 'Start_time',
                    'val': entry.start_time.strftime('%X') if entry.start_time else '',
                },
                {
                    'col': 'End_time',
                    'val': entry.end_time.strftime('%X') if entry.end_time else '',
                },
                {
                    'col': 'Date',
                    'val': entry.start_time.strftime('%m/%d/%Y') if entry.start_time else '',
                },
                {
                    'col': 'Auditor',
                    'val': entry.auditor.username,
                },
            ]

            # route items
            route_items = RouteItem.objects.filter(survey=entry.survey).order_by('position')
            route_section = EntryRouteSection.objects.filter(entry=entry)
            if route_items.exists():
                cols += self._entry_items_for_section_items(route_section, route_items, section_name='route')

            # segment items
            segment_items = SegmentItem.objects.filter(survey=entry.survey).order_by('position')
            segment_sections = EntrySegmentSection.objects.filter(entry=entry)
            for i, section in enumerate(segment_sections):
                cols += [
                    {
                        'col': 'S%s_ID' % (i+1),
                        'val': section.segment_id if section.segment_id else '',
                    },
                    {
                        # street
                        'col': 'S%s_Segment' % (i+1),
                        'val': section.street if section.street else '',
                    },
                    {
                        'col': 'S%s_Side' % (i+1),
                        'val': section.side if section.side else '',
                    },
                    {
                        'col': 'S%s_Xstreet1' % (i+1),
                        'val': section.starting_xstreet if section.starting_xstreet else '',
                    },
                    {
                        'col': 'S%s_Xstreet2' % (i+1),
                        'val': section.ending_xstreet if section.ending_xstreet else '',
                    },
                ]
                cols += self._entry_items_for_section_items(section, segment_items, section_name='segment', section_index=i+1)

            # crossing items
            crossing_items = CrossingItem.objects.filter(survey=entry.survey).order_by('position')
            crossing_sections = EntryCrossingSection.objects.filter(entry=entry)
            for i, section in enumerate(crossing_sections):
                cols += [
                    {
                        'col': 'C%s_ID' % (i+1),
                        'val': section.crossing_id if section.crossing_id else '',
                    },
                    {
                        'col': 'C%s_Xstreet1' % (i+1),
                        'val': section.intersection1 if section.intersection1 else '',
                    },
                    {
                        'col': 'C%s_Xstreet2' % (i+1),
                        'val': section.intersection2 if section.intersection2 else '',
                    },
                    {
                        'col': 'C%s_Side1' % (i+1),
                        'val': section.crossing_from if section.crossing_from else '',
                    },
                    {
                        'col': 'C%s_Side2' % (i+1),
                        'val': section.crossing_to if section.crossing_to else '',
                    },
                ]
                cols += self._entry_items_for_section_items(section, crossing_items, section_name='crossing', section_index=i+1)

            # culdesac items
            culdesac_items = CuldesacItem.objects.filter(survey=entry.survey).order_by('position')
            culdesac_sections = EntryCuldesacSection.objects.filter(entry=entry)
            for i, section in enumerate(culdesac_sections):
                cols += [
                    {
                        'col': 'D%s_ID' % (i+1),
                        'val': section.culdesac_id if section.culdesac_id else '',
                    },
                    {
                        'col': 'D%s_Street_name' % (i+1),
                        'val': section.street if section.street else '',
                    },
                ]
                cols += self._entry_items_for_section_items(section, culdesac_items, section_name='culdesac', section_index=i+1)

            rows.append(cols)

        # sort rows by the most columns so the sections print out (hopefully) grouped together
        rows = sorted(rows, key=lambda x: len(x), reverse=True)

        # build column row
        columns = []
        for row in rows:
            for data in row:
                if data['col'] not in columns:
                    columns.append(data['col'])

        # build data rows
        rows_values = []
        for row in rows:
            row_values = []
            for col in columns:
                exists = False
                for data in row:
                    if data['col'] == col:
                        row_values.append(data['val'])
                        exists = True
                        break
                if not exists:
                    row_values.append(None)
            rows_values.append(row_values)

        # don't export csv, just render table in browser
        if self.render_in_browser:
            return render(request, 'entries/export.html', {
                'cols': columns,
                'rows_values': rows_values,
                'title': 'CSV Export',
                'survey_version': entries[0].survey.version if entries else '',
            })

        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="maps_export.csv"'

        writer = csv.writer(response)
        writer.writerow(columns)
        for row in rows_values:
            writer.writerow(row)
        return response

    def _entry_items_for_section_items(self, section, section_items, section_name=None, for_sub_item=False, subitem_prefix_count=None, section_index=None):
        """
        :type section_items : list of maps.models.Item
        """

        data = []
        prefix_count = {}

        for i, item in enumerate(section_items):

            # tally up each prefix section so we can calculate the column codes
            prefix_count[item.code_prefix.prefix] = prefix_count.get(item.code_prefix.prefix, 0) + 1

            if item.type == SUB_ITEM:
                data += self._entry_items_for_section_items(
                    section,
                    item.subitem_set.all().order_by('position'),
                    section_name=section_name,
                    for_sub_item=True,
                    subitem_prefix_count=prefix_count[item.code_prefix.prefix],
                    section_index=section_index)
            else:
                item_options = SECTION_CLASSES[section_name][ITEM_OPTION].objects.filter(option__item=item, section=section)
                sub_item_options = SECTION_CLASSES[section_name][SUB_ITEM_OPTION].objects.filter(option__item=item, section=section)
                item_aux = SECTION_CLASSES[section_name][ITEM_AUXILIARY].objects.filter(item=item, section=section)
                sub_item_aux = SECTION_CLASSES[section_name][SUB_ITEM_AUXILIARY].objects.filter(item=item, section=section)
                item_na = SECTION_CLASSES[section_name][ITEM_NA].objects.filter(item=item, section=section)
                sub_item_na = SECTION_CLASSES[section_name][SUB_ITEM_NA].objects.filter(item=item, section=section)

                # "N/A" for select multiple gets coded as 0
                # "N/A" for select and gets coded as NOT_APPLICABLE

                if item.type == SELECT:

                    if for_sub_item:
                        data.append({
                            'col': self._build_col_name(item, subitem_prefix_count, section_index=section_index, suffix=ALPHABET[i]),
                            'val': sub_item_options[0].option.value if sub_item_options.exists() else NOT_APPLICABLE if sub_item_na.exists() else '',
                        })
                    else:
                        data.append({
                            'col': self._build_col_name(item, prefix_count[item.code_prefix.prefix], section_index=section_index),
                            'val': item_options[0].option.value if item_options.exists() else NOT_APPLICABLE if item_na.exists() else '',
                        })
                elif item.type == SELECT_MULTIPLE:
                    if for_sub_item:
                        for k, option in enumerate(item.itemoption_set.all()):
                            data.append({
                                'col': self._build_col_name(item, subitem_prefix_count, section_index=section_index, suffix=ALPHABET[k+subitem_prefix_count-1]),
                                'val': sub_item_options.filter(option=option)[0].option.value if sub_item_options.filter(option=option).exists() else '0',
                            })
                    else:
                        # we don't have to look for an N/A item because the rest of the items just get assigned "0"
                        for k, option in enumerate(item.itemoption_set.all()):
                            data.append({
                                'col': self._build_col_name(item, prefix_count[item.code_prefix.prefix], section_index=section_index, suffix=ALPHABET[k]),
                                'val': item_options.filter(option=option)[0].option.value if item_options.filter(option=option).exists() else '0',
                            })
                elif item.type in [TEXT, INTEGER]:
                    if for_sub_item:
                        data.append({
                            'col': self._build_col_name(item, subitem_prefix_count, section_index=section_index, suffix=ALPHABET[i]),
                            'val': sub_item_aux[0].value if sub_item_aux.exists() else ''
                        })
                    else:
                        data.append({
                            'col': self._build_col_name(item, prefix_count[item.code_prefix.prefix], section_index=section_index),
                            'val': item_aux[0].value if item_aux.exists() else ''
                        })
                # couldn't find an appropriate item type (shouldn't happen)
                else:
                    data.append({
                        'col': '%s%s' % (item.code_prefix.prefix, prefix_count[item.code_prefix.prefix]),
                        'val': '[UNKNOWN TYPE]',
                    })

        return data

    def _build_col_name(self, item, item_index, section_index=None, suffix=None):

        # every section except for "Route" should have this
        if section_index:
            col_prefix = '%s%s_%s' % (item.code_prefix.prefix, section_index, item_index)
        else:
            col_prefix = '%s%s' % (item.code_prefix.prefix, item_index)

        if suffix:
            col_prefix += suffix

        return col_prefix
