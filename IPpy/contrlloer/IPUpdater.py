import time

from IPpy.service.scanIP import getAliveIP

while(1):
    iplist = getAliveIP()
    print iplist
    time.sleep(120)



