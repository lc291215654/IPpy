# -*- coding: utf-8 -*-
from django.shortcuts import render

from IPpy.models import IpInfo

#flag 1 : 注册正在使用
#     2 : 注册未使用
#     3 : 未注册在使用
#     4 : 空闲


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
        ip = IpInfo.objects.filter(ipaddr=ipaddr)
        ip1 = ip.get()
        if ip1.flag == 1:
            ip1.username = ' '
            ip1.describe = ' '
            ip1.flag = 3

        elif ip1.flag == 2:
            ip1.username = ' '
            ip1.describe = ' '
            ip1.flag = 4

        elif ip1.flag == 3:
            ip1.username = request.POST['username']
            ip1.describe = request.POST['describe']
            ip1.flag = 1

        elif ip1.flag == 4:
            ip1.username = request.POST['username']
            ip1.describe = request.POST['describe']
            ip1.flag = 2

       # ip1.save(update_fields=['flag'])
        ip1.save()

        context['success'] = "success"
    return render(request, 'register.html', context)