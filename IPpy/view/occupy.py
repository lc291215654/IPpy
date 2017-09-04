from django.shortcuts import render

from IPpy.models import IpInfo


def index(request):
    iplist = IpInfo.objects.filter(flag=3)
    context = {}
    context['occupy_list'] = iplist
    return render(request, 'occupy.html', context)