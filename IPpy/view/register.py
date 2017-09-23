# -*- coding: utf-8 -*-
from django.shortcuts import render

from IPpy.models import IpInfo


def index(request):
    context = {}
    #样例^-^
    athlete_list = ['a', 'af']
    context['athlete_list'] = athlete_list
    # 样例end

    if 'id' in request.GET:
        ip = IpInfo.objects.filter(id=request.GET['id'])
        context['ip'] = ip

    if request.POST:
        ipaddr = request.POST['ipaddr']
        username = request.POST['username']
        describe = request.POST['describe']
        ip = IpInfo.objects.filter(ipaddr=ipaddr)
        ip1 = ip.get()
        ip1.username=username
        ip1.describe=describe
        ip1.flag=2
        ip1.save()
    return render(request, 'register.html', context)