import time

from IPpy.service.scanIP import getAliveIP
import thread
import threading

class IPUpdater(threading.Thread):

    flag = 0

    def scanDeamon(self):
        while(self.flag):

            #   iplist = getAliveIP()
            #     print iplist
            time.sleep(120)

    def run(self):
        while (self.flag):
            print "Starting " + self.name
            print "^^^^^"
            print "Exiting " + self.name

    def setFlag(self):
        self.flag = 1

    def unsetFlag(self):
        self.flag = 0

    def getFlag(self):
        return self.flag
