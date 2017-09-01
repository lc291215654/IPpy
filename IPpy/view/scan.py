from django.shortcuts import render

from IPpy.contrlloer.IPUpdater import IPUpdater

flag = 0

def index(request):
    global flag
    ipupdater = IPUpdater()
    context = {}
    request.encoding = 'utf-8'

    if 'start' in request.GET:
        if ipupdater.getFlag() == 0 and 0 == flag :
            ipupdater.setFlag()
            ipupdater.start()
            flag = 1
        context['start'] = flag

    if 'stop' in request.GET:

        if 0 == flag:
            context['stop'] = 1
        else:
            context['stop'] = 0

        ipupdater.unsetFlag()

    return render(request, 'scan.html', context)

