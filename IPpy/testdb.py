# -*- coding: utf-8 -*-

from django.http import HttpResponse

from models import IpInfo


# 数据库操作
def testdb(request):
    test1 = IpInfo(ipaddr='192.168.1.101')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")