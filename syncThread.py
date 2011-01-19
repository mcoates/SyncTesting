'''
Created on Dec 4, 2010

@author: Michael Coates - mcoates@mozilla.com

This is test code. No guarantees if you use this for anything.
'''
import threading
import time
from myHttpRequest import myHttpRequest
import random

class ClientThread ( threading.Thread):

    # Note that we do not override Thread's __init__ method.
    # The Queue module makes this not necessary.
    def __init__(self,coordinatorObj):
        threading.Thread.__init__(self)
        self.myCoordinator=coordinatorObj
    def setCoordinator(self, coordinatorObj):
        self.myCoordinator=coordinatorObj
    def run (self):
        #self.myCoordinator=coordinatorObj
        # Have our thread serve "forever":
        while True:
            #print "%s: Queue Size %i\n" % (self.getName(), clientPool.qsize())
            
            # Get a client out of the queue, add False to not block
            #print "My Coordinator: %s" % self.myCoordinator
            client = self.myCoordinator.getClient()
            message="Reporting in from thread %s" % self.name
            #self.myCoordinator.report(message)
            #time.sleep(3)
            #client =counterVal
            #print "Getting a thread client named %s" % self.getName()
            # Check if we actually have an actual client in the client variable:
            if client != None:
                #print "%s: I'm Alive" % self.getName()
                self.doAction(client)
                #print "%s: I'm Done - going to sleep" % self.getName()
                #time.sleep(3)
                #print "Global Value is %i " % globalVal
            elif client == None:
                 print "%s: Failed to get client" % (self.getName())
    def doAction(self, clientData):
        staticKeyExchangePortion= "d3361865e53d1d7c5a1fa70481fe988c34a29e4acfafb16362dc0b73905a207bfed485d6e52ebefd14c26cb79247f24e5dfaf931e574c39acdecba375e81a560b00a311765cc02b5a4d01804955e7256317418af1cc1fb84ae"
        #print "%s: Doing stuff with %s" % (self.getName(), clientData)
        httpObject = myHttpRequest()  
        #This should really come from a config file
        httpObject.host = "fill me in - no http or www"
        httpObject.url = "http://fill me in"
        httpObject.method = "GET"
        httpObject.prepareHeaders()
        randomId=(str(random.getrandbits(256))+staticKeyExchangePortion).zfill(256)
        httpObject.headers["x-keyexchange-id"] = randomId 
        httpObject.sendRequest()    
        self.myCoordinator.countResult(httpObject.getResponse()) 
        self.myCoordinator.report(self.name+": "+httpObject.getResponse())
        
        