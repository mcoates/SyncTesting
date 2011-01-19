'''
Created on Dec 4, 2010

@author: Michael Coates - mcoates@mozilla.com

This is test code. No guarantees if you use this for anything.

If you want this to work update the following two variables in syncThread
        httpObject.host = ""
        httpObject.url = ""
'''

import Queue
import time
from syncThread import ClientThread
from decimal import Decimal

class Coordinator ():
    print "main"

    # Create our Queue:
    def __init__(self):
        self.clientPool = Queue.Queue ( 0 )
        self.name="Coordinator!"
        self.failed=0
        self.passed=0
    def insertClient(self, val):
        self.clientPool.put(val)
    def getClient(self):
        return self.clientPool.get()
    def report(self, message):
        #pass
        print "%s , %s" % ((message), time.strftime("%X"))
    def getSize(self):
        #this is an estimate
        return self.clientPool.qsize()
    def countResult(self, httpResponse):
        #print "count"
        if "You don't have permission to access" in httpResponse:
            self.failed=self.failed+1
        else:
            self.passed=self.passed+1

coordinator=Coordinator()
# Start worker threads:
print "Creating Working Threads"
for x in xrange ( 5 ):
    #time.sleep(.5)
    newThread=ClientThread(coordinator)
    #newThread.setCoordinator(coordinator)
    newThread.start()
print "Working Threads Ready"
time.sleep(1)
print "Populating Work Queue"
start = time.time()
#Number of Items To Iterate - this is overkill design for this app,
for y in xrange(500):
    #print "Master!!: adding Val%s" % (y)
    coordinator.insertClient("Val%s" % y)  

while coordinator.getSize()!=0:
    pass

time.sleep(1)
end = time.time()
elapsed= end - start

print "Your stuff took", elapsed, "seconds to run"
print "Got Channels for: %s " % (coordinator.passed)
print "Denied Channels for: %s " % (coordinator.failed)
print "Succes Ratio " ,Decimal(coordinator.passed)/ Decimal(coordinator.failed+coordinator.passed)
exit()