# -*- coding: utf-8 -*-

from django.http import HttpResponse

from IPpy.models import IpInfo


# 数据库操作
from IPpy.service.scanIP import getAliveIP


def testdb(request):
    iplist = getAliveIP()
    for ip in iplist.get("iplist"):
        test1 = IpInfo(ipaddr=ip,create_at='2017-08-31 22:26:53',flag=1)
        test1.save()
    return HttpResponse("<p>数据添加成功！</p>")