from django.shortcuts import render

from IPpy.models import IpInfo


def index(request):
    iplist = IpInfo.objects.filter(flag=4)
    context = {}
    context['available_list'] = iplist
    return render(request, 'available.html', context)