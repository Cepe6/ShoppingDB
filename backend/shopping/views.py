# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import User, Cart

# Create your views here.
def user(request):
    users = User.objects.all()
    response = []
    for u in users:
        response.append({
                    "id": u.id,
                    "name" : u.name
                })
    return JsonResponse(response, safe = False)
