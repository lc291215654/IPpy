from django.shortcuts import render

from IPpy.models import IpInfo


def index(request):
    iplist = IpInfo.objects.all()
    context = {}
    context['athlete_list'] = iplist



    return render(request, 'index.html', context)