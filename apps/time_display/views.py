# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
# from time import localtime, strftime
from django.utils import timezone

# Create your views here.
def index(request):
    now = timezone.now()
    context = {
        "date": now.strftime("%b %d, %Y"),
        "time": now.strftime("%I:%M %p")
    }
    return render(request, 'time_display/index.html', context)