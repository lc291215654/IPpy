# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

from IPpy.models import IpInfo


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    athlete_list=['a','af']
    context['athlete_list'] = athlete_list

    return render(request, 'hello.html', context)

def hello2(request):
    context = {}
    context['hello'] = 'Hello World!'
    athlete_list=['a','af']
    context['athlete_list'] = athlete_list

    return render(request, 'hello2.html', context)

# 数据库操作
def testdb(request):
    test1 = IpInfo(ipaddr='192.168.1.101')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")