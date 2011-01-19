'''
Created on Sep 7, 2010

@author: Michael Coates - mcoates@mozilla.com

This is test code. No guarantees if you use this for anything.
'''
import httplib
class myHttpRequest: 
    
    def __init__(self):
        self.note = ""
        self.host = ""
        self.url = ""
        self.method = ""
        self.headers = {}
        self.body = ""
        self.responseData ="";
        
    def printRequest(self):
        print "hello from object %s" % (self)
    
    def sendRequest(self):
        #print "Sending Request - %s" % self.url 
        if self.url.startswith("http://"):
            conn = httplib.HTTPConnection(self.host)
        elif self.url.startswith("https://"):
            conn = httplib.HTTPSConnection(self.host)
        else:
            print "ERROR - URL does not contain protocol"
        self.headers["host"]=self.host
        #print self.headers
        conn.request(self.method, self.url, self.body, self.headers)       
       
        r = conn.getresponse()
        status = r.status
        responseData = r.read()
        #print "Response HTTP Status %s " % (status)
        self.responseData=responseData
        
    def printResponse(self):
        print self.responseData
        
    def getResponse(self):
        return self.responseData
    
    def prepareHeaders(self):
        headers={}
        headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b8pre) Gecko/20101127 Firefox/4.0b8pre"
        headers["Accept-Language"] = "en-us,en;q=0.5"
        headers["Accept-Encoding"] = "gzip, deflate"
        headers["Accept-Charset"] = "ISO-8859-1,utf-8;q=0.7,*;q=0.7"
        headers["Keep-Alive"] = "115"
        headers["Connection"] = "keep-alive"
        headers["x-keyexchange-id"] = "4ba8db10efc6e90313b1f68da377404ee47c0f3dbddba265d79f878ec9d063ed490e0427f63013d3361865e53d1d7c5a1fa70481fe988c34a29e4acfafb16362dc0b73905a207bfed485d6e52ebefd14c26cb79247f24e5dfaf931e574c39acdecba375e81a560b00a311765cc02b5a4d01804955e7256317418af1cc1fb84ae"
        self.headers = headers
       
        
    def sendXMLRequestREFERENCE(self, site, url, body,bugzillaCookie,base64string):
        #url="/xmlrpc.cgi"
        #url="/show_bug.cgi?id=11383"
        #site ="127.0.0.1:8081"
        #body ="<methodCall><methodName>Splinter.check_can_access</methodName><params><param><value><struct><member><name>attachment_id</name><value><value><int>456154</int></value></value></member><member><name>review</name><value><value><string></string></value></value></member></struct></value></param></params></methodCall>"
        headers = {'Host': site,
                   "X-Requested-With": "XMLHttpRequest",
                   "Content-Type": "text/xml; charset=UTF-8",
                   "Accept-Encoding": "gzip, deflate",
                   "Cookie": bugzillaCookie,
                   "Authorization": "Basic "+base64string}
        conn2 = httplib.HTTPSConnection(site)
        conn2.request("POST", url, body, headers) 
        #print conn.request   
        r2 = conn2.getresponse()
        data = r2.read()
        print "body request"
        print body
        print "response"
        print data
        
        print "============================="