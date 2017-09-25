# -*- coding: utf-8 -*-

from django.http import HttpResponse

from IPpy.models import IpInfo
from IPpy.service.scanIP import getAliveIP

# 数据库操作
def testdb(request):
    #test1 = IpInfo(ipaddr='192.168.1.101')
    iplist = IpInfo.objects.all()
    for ip in iplist:
        if ip.flag == 2:
            ip.flag = 4
            #ip.save()
    return HttpResponse("<p>数据添加成功！</p>")


def testdb2(request):
    iplist = getAliveIP()
    for ip in iplist.get("iplist"):
        test1 = IpInfo(ipaddr=ip,create_at='2017-08-31 22:26:53',flag=1)
        test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
