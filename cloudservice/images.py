#
# Copyright (c) 2010, iPlant Collaborative, University of Arizona, Cold Spring Harbor Laboratories, University of Texas at Austin
# This software is licensed under the CC-GNU GPL version 2.0 or later.
# License: http://creativecommons.org/licenses/GPL/2.0/
#
# Author: Seung-jin Kim
# Contact: seungjin@email.arizona.edu
# Twitter: @seungjin
#

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from django.http import HttpResponse, Http404
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.contrib.auth import logout

from django.http import HttpResponseNotFound
from django.http import HttpResponseForbidden

from django.utils import simplejson
import logging

from atmosphere.cloudservice.models import *

from atmosphere.cloudservice.user import *



import token_validation

import getopt, sys, os
from euca2ools import Euca2ool, InstanceValidationError, Util
from django.utils import simplejson
    

def image(request) :
    
  if token_validation.validate_access(request) == True :

    method = request.META['REQUEST_METHOD']
    username = request.META['HTTP_X_AUTH_USER']
    api_server_url = request.META['HTTP_X_AUTH_API_SERVER']
    token = request.META['HTTP_X_AUTH_TOKEN']

    if method == "GET" :
      return_json = getImage(username,token,api_server_url)
    else :
      return HttpResponse("HTTP ERROR!")

    return HttpResponse(return_json)


  else :
    return HttpResponse("401 UNAUTHORIZED", status=401)


def getImage(username,token,api_server_url):
  user = User(username,token,api_server_url)
  return user.user_ec2_access_key
