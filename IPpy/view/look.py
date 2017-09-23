from django.shortcuts import render

from IPpy.models import IpInfo


def index(request):
    context = {}
    if request.POST:
        context['rlt'] = request.POST['q']
    return render(request, 'look.html', context)