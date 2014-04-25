import urllib2
from launch import *


def proxy_mangle_request(req):
    if ("google.com" in req.url):
        q.put(('bbbb', 139.1, -47.8, 0.86))
        print "sitestat:"+str((q.qsize()))
        #print url


def proxy_mangle_response(res):
    return res
