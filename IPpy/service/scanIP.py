import commands
import re

import time


def getAliveIP():
    status , output = commands.getstatusoutput("nmap -sP 192.168.142.0/24")

    iplist = []

    for linea in output.split("\n"):
        if linea.find("192.168.142.")>1:
            ip =  re.findall(r'\d+.\d+.\d+.\d+',linea)
            iplist.append(ip.pop())

    dictIP = {}
    dictIP['time'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    dictIP['iplist'] = iplist
    return dictIP



