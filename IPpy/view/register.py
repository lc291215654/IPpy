from django.shortcuts import render

from IPpy.models import IpInfo


def index(request):
    context = {}
    return render(request, 'register.html', context)