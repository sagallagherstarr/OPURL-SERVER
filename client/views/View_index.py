#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        views.View_index.py
# Purpose:
#
# Author:      scott
#
# Created:     30/07/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##import os.path
##import logging

from kay.app import get_application

from kay.utils import (
  render_to_response,
)

from kay.handlers import (
  BaseHandler,
)

# Create your views here.

class IndexRequest(BaseHandler):
  def get(self):
##    appp = get_application()
##    set_trace()
    return render_to_response('client/index.html')

index = IndexRequest()