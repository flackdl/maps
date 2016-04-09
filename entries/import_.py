import csv
from django import forms
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from entries.models import Entry
from maps.models import Survey

COLUMNS = (
    ('survey', 'Survey Version / Name', 'Abbreviated'),
    ('auditor', "Auditor's username", 'bob'),
    ('route', 'Route Number', '1001'),
    ('starting_address', '', '123 Main st'),
    ('ending_address', '', '456 End Blvd')
)


class UploadFileForm(forms.Form):
    file = forms.FileField()


class Import(View):

    def _default_context(self):
        return {'form': UploadFileForm, 'expected_columns': COLUMNS}

    def post(self, request, *args, **kwargs):

        result = self._default_context()
        result.update({'success': True, 'submitted': True})

        columns_sorted = [col[0] for col in COLUMNS]
        columns_sorted.sort()
        header = None
        rows = []

        file = request.FILES.get('file')

        if not file:
            result.update({'success': False, 'messages': ['Please upload a .csv file']})
            return render(request, 'entries/import.html', result)

        try:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                # capture the header row
                if i == 0:
                    header = list(row)
                    header_sorted = list(header)
                    header_sorted.sort()
                    continue
                else:
                    rows.append(row)
        except:
            result.update({'success': False, 'messages': ['Please upload a valid .csv file']})
            return render(request, 'entries/import.html', result)

        # column headers aren't as expected
        if cmp(header_sorted, columns_sorted) != 0:
            result.update({
                'success': False,
                'submitted': True,
                'messages': [
                    'Got incorrect columns: %s' % (','.join(header)),
                    'Expecting columns %s' % (','.join(columns_sorted)),
                ]
            })

        else:
            bad_rows = []
            imported_rows = []
            for i, row in enumerate(rows):
                auditor = row[header.index('auditor')]
                survey_name = row[header.index('survey')]
                route = row[header.index('route')]
                starting_address = row[header.index('starting_address')]
                ending_address = row[header.index('ending_address')]

                try:
                    user = User.objects.get(username=auditor)
                except User.DoesNotExist:
                    bad_rows.append('row %s: username "%s" does not exist in the system (%s)' %
                                    (i+2, auditor, ', '.join(row)))
                    continue
                try:
                    survey = Survey.objects.get(version=survey_name)
                except Survey.DoesNotExist:
                    bad_rows.append('row %s: survey version "%s" does not exist in the system (%s)' %
                                    (i+2, survey_name, ', '.join(row)))
                    continue

                Entry(
                    auditor=user,
                    survey=survey,
                    starting_address=starting_address if starting_address else None,
                    ending_address=ending_address if ending_address else None,
                    route_number=route,
                    start_time=None,
                    end_time=None,
                    submitted=None,
                ).save()

                imported_rows.append(row)

            result.update({'imported_rows': imported_rows})
            result.update({'bad_rows': bad_rows})

        return render(request, 'entries/import.html', result)

    def get(self, request, *args, **kwargs):
        return render(request, 'entries/import.html', self._default_context())
