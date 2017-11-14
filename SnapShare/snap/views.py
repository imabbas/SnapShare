# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Aadil")

def user_profile(request, user_id):
    return HttpResponse("This is the profile for user %s."  % user_id)

# Create your views here.
