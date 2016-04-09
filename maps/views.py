import re
import urllib
import json
from os import path, listdir
from django.contrib.auth import logout
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from maps.models import RouteItem, Survey, SegmentItem, CrossingItem, CuldesacItem
from maps.utils import build_item


def survey_items(request):

    response = []

    for survey in Survey.objects.filter(published=True):

        survey_response = {
            'id': survey.id,
            'title': survey.version,
            'survey_type': survey.type.slug if survey.type else None
        }

        survey_parts = [
            {
                'part': 'route',
                'items': RouteItem.objects.filter(survey=survey).order_by('survey__id', 'position')
            },
            {
                'part': 'segment',
                'items': SegmentItem.objects.filter(survey=survey).order_by('survey__id', 'position'),
                'required_form_fields': ['street', 'side', 'starting_xstreet', 'ending_xstreet'],
            },
            {
                'part': 'crossing',
                'items': CrossingItem.objects.filter(survey=survey).order_by('survey__id', 'position'),
                'required_form_fields': ['intersection1', 'intersection2', 'crossing_from', 'crossing_to'],
            },
            {
                'part': 'culdesac',
                'items': CuldesacItem.objects.filter(survey=survey).order_by('survey__id', 'position'),
                'required_form_fields': ['street'],
            },
        ]

        for survey_part in survey_parts:
            items = []
            for item in survey_part['items']:
                items.append(build_item(item))

            survey_response.update({
                '%s_items' % survey_part['part']: items,
                '%s_required_form_fields' % survey_part['part']: survey_part.get('required_form_fields')
            })

        response.append(survey_response)

    return HttpResponse(json.dumps(response), content_type="application/json")


def base(request):
    return render(request, 'maps/base.html')


@csrf_exempt
def ng_logout(request):
    logout(request)
    return HttpResponse(json.dumps({'success': True}))


def ng_dashboard(request):
    return render(request, 'maps/dashboard.html')


def ng_add_route(request):
    return render(request, 'maps/add_route.html')


def ng_route(request):
    return render(request, 'maps/route.html')


# cache manifest
def manifest(request):
    uploads_dir = '%s/uploads' % settings.MEDIA_ROOT
    uploads_path = '%suploads' % settings.MEDIA_URL

    resources = []

    for f in listdir(uploads_dir):
        if path.isfile(path.join(uploads_dir, f)):
            # skip thumbnails, medium, and large versions
            if re.search(r'_(thumbnail|medium|big|large)\.\w+$', f):
                continue
            resources.append('%s/%s' % (uploads_path, urllib.quote_plus(f)))

    return render(request, 'maps/manifest.html', {'resources': resources}, content_type='text/cache-manifest')
