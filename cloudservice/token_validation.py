#
# Copyright (c) 2010, iPlant Collaborative, University of Arizona, Cold Spring Harbor Laboratories, University of Texas at Austin
# This software is licensed under the CC-GNU GPL version 2.0 or later.
# License: http://creativecommons.org/licenses/GPL/2.0/
#
# Author: Seung-jin Kim
# Contact: seungjin@email.arizona.edu
# Twitter: @seungjin
#

import httplib, urllib


def validate_access(request):
    return True

"""
    if request.META.has_key('HTTP_X_AUTH_USER') and request.META.has_key('HTTP_X_AUTH_TOKEN') and request.META.has_key('HTTP_X_AUTH_API_SERVER') :
        
        username = request.META['HTTP_X_AUTH_USER']
        token = request.META['HTTP_X_AUTH_TOKEN'] 
        api_server_url = request.META['HTTP_X_AUTH_API_SERVER']
        
        auth_server_ip = "150.135.78.195"
        port = 8000
        path = "/auth/validate_token"
        method = "GET"
        params = urllib.urlencode(request.GET)
        headers = {
            "Content-type" : "application/x-www-form-urlencoded",
            "Accept" : "text/plain",
            "X-Auth-User" : username,
            "X-Auth-Token" : token,
            "X-Auth-Api-Server": api_server_url
        }

        co = httplib.HTTPConnection(auth_server_ip,port)
        #co.request(method,path,params,headers)
        #r1 = conn.getresponse()
        #print r1.status
        #co.close()
        return "a"
    else :
        return "b"
"""
    