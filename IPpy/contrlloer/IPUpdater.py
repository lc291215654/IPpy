# -*- coding: utf-8 -*-
import time

from IPpy.models import IpInfo
from IPpy.service.scanIP import getAliveIP
import threading

class IPUpdater(threading.Thread):

    def run(self):
        while 1:
            self.updateIP()
            time.sleep(120)

    def updateIP(self):
        ipdic = getAliveIP()
        curtime = ipdic['time']
        iplist = ipdic['iplist']

        # 更新扫描到的IP
        for ip in iplist:
            ipmodel = IpInfo.objects.filter(ipaddr=ip)
            if ipmodel.count() == 0:
                addip = IpInfo(ipaddr=ip,flag=3,create_at=curtime)
                addip.save()
            else:
                for ipk in ipmodel:
                    if ipk.flag == 4:
                        ipk.flag = 3
                        ipk.save()
                    if ipk.flag == 2:
                        ipk.flag = 1
                        ipk.save()
            print ip

        # 更新未扫描到的IP
        for ip in IpInfo.objects.all():
            print iplist.index(ip)
            # if iplist.(ip.addr):




