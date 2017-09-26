# -*- coding: utf-8 -*-
import time

from IPpy.models import IpInfo
from IPpy.service.scanIP import getAliveIP
import threading

class IPUpdater(threading.Thread):

    def run(self):
        while 1:
            self.updateIP()
            time.sleep(180)

    def updateIP(self):
        ipdic = getAliveIP()
        curtime = ipdic['time']
        iplist = ipdic['iplist']

        # 更新扫描到的IP
        for ipstr in iplist:
            ipmodel = IpInfo.objects.filter(ipaddr=ipstr)
            if ipmodel.count() == 0:
                addip = IpInfo(ipaddr=ipstr,flag=2,create_at=curtime)
                addip.save()
            else:
                for ipk in ipmodel:
                    if ipk.flag == 4:
                        ipk.flag = 3
                    elif ipk.flag == 2:
                        ipk.flag = 1
                    ipk.save()

        # 更新未扫描到的IP
        for ip in IpInfo.objects.all():
            if ip.ipaddr not in iplist:
                if ip.flag == 3:
                    ip.flag = 4
                elif ip.flag == 1:
                    ip.flag = 2
                ip.save()





            # if iplist.(ip.addr):




