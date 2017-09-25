from django.shortcuts import render

from IPpy.models import IpInfo


def index(request):
    context = {}
    if request.POST:
        username = request.POST['username']
        iplist = IpInfo.objects.filter(username=username)
        context['athlete_list'] = iplist
    return render(request, 'look.html', context)