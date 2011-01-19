'''
Created on Nov 29, 2010

@author: Michael Coates - mcoates@mozilla.com

This is test code. No guarantees if you use this for anything.

If you want this to work update the following two variables that are located in the code below
        httpObject.host = ""
        httpObject.url = ""
'''
from myHttpRequest import myHttpRequest
from time import gmtime, strftime
import datetime, time
import threading, random
from decimal import Decimal


if __name__ == '__main__':
    print "running"
    i=0
    failed=0
    passed=0
    headers={}
    httpObject = myHttpRequest()  
    
    httpObject.host = "fill me in - no http or www"
    httpObject.url = "http://fill me in"
    httpObject.method = "GET"
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b8pre) Gecko/20101127 Firefox/4.0b8pre"
    headers["Accept-Language"] = "en-us,en;q=0.5"
    headers["Accept-Encoding"] = "gzip, deflate"
    headers["Accept-Charset"] = "ISO-8859-1,utf-8;q=0.7,*;q=0.7"
    headers["Keep-Alive"] = "115"
    headers["Connection"] = "keep-alive"
    #256 characters 0-9a-z
    headers["x-keyexchange-id"] = "4ba8db10efc6e90313b1f68da377404ee47c0f3dbddba265d79f878ec9d063ed490e0427f63013d3361865e53d1d7c5a1fa70481fe988c34a29e4acfafb16362dc0b73905a207bfed485d6e52ebefd14c26cb79247f24e5dfaf931e574c39acdecba375e81a560b00a311765cc02b5a4d01804955e7256317418af1cc1fb84ae"
    staticKeyExchangePortion= "d3361865e53d1d7c5a1fa70481fe988c34a29e4acfafb16362dc0b73905a207bfed485d6e52ebefd14c26cb79247f24e5dfaf931e574c39acdecba375e81a560b00a311765cc02b5a4d01804955e7256317418af1cc1fb84ae"
    httpObject.headers = headers
    httpObject.body = ""

    start = time.time()
    
    while i<3000:
               
        randomId=(str(random.getrandbits(256))+staticKeyExchangePortion).zfill(256)
        httpObject.headers["x-keyexchange-id"] = randomId 
        #print httpObject.headers["x-keyexchange-id"]
        i=i+1
        print i, " ", 
        httpObject.sendRequest()       
        httpResponse = httpObject.getResponse() 
        print httpObject.getResponse()," ", time.strftime("%X")
                #print "count"
        if "You don't have permission to access" in httpResponse:
            failed=failed+1
        else:
            passed=passed+1
    print "--------------------------"
    print "done"
    # Do Stuff Here
    end = time.time()
    elapsed= end - start
    print "Your stuff took", elapsed, "seconds to run"
    print "Got Channels for: %s " % (passed)
    print "Denied Channels for: %s " % (failed)
    print "Succes Ratio " ,Decimal(passed)/ Decimal(failed+passed)