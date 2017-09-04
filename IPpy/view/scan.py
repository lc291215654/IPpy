# -*- coding: utf-8 -*-
from django.shortcuts import render
from IPpy.contrlloer import IPUpdater

def index(request):
    context = {}
    request.encoding = 'utf-8'

    if 'start' in request.GET:
        ipupdater = IPUpdater.IPUpdater()
        ipupdater.start()
        context['start'] = 1
    return render(request, 'scan.html', context)

