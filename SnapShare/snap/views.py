# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'snap/home.html')

def user_profile(request, user_id):
    myString = str("This is the profile for user %s."  % user_id)
    context = {
        "myString": myString,
    }
    return render(request, 'snap/base.html', context)

def login(request):
    return render(request, 'snap/login.html')

def register(request):
    return render(request, 'snap/register.html')


# Create your views here.
