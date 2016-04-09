import json
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt


class Login(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(Login, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'maps/login.html')

    def post(self, request):

        credentials = json.loads(request.body)

        username = credentials.get('username')
        password = credentials.get('password')

        user = authenticate(username=username, password=password)

        # successfully logged in
        if user is not None:
            login(request, user)
            return HttpResponse(json.dumps({'success': True,  'username': user.username}),
                                content_type="application/json")

        return HttpResponse(json.dumps({'success': False}), content_type="application/json")
