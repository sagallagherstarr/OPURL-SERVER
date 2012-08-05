#-------------------------------------------------------------------------------
# Name:        views.__init__.py
# Purpose:
#
# Author:      scott
#
# Created:     30/07/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
client.views
"""

"""
import logging

from google.appengine.api import users
from google.appengine.api import memcache
from werkzeug import (
  unescape, redirect, Response,
)
from werkzeug.exceptions import (
  NotFound, MethodNotAllowed, BadRequest
)

from kay.utils import (
  render_to_response, reverse,
  get_by_key_name_or_404, get_by_id_or_404,
  to_utc, to_local_timezone, url_for, raise_on_dev
)
from kay.i18n import gettext as _
from kay.auth.decorators import login_required

"""
import logging
import json
import zipfile

from google.appengine.datastore.datastore_query import Cursor

from werkzeug import datastructures

from kay.utils import forms

from kay.utils import render_to_response, set_trace
from kay.utils.paginator import Paginator

from kay.handlers import BaseHandler

from client.forms import XLSFileUploadForm

#from lib.openpyxl.reader.excel import load_workbook

from client.models import SampleStorage

##from index import index

#from lib.pyExcelerator.CompoundDoc import Reader
##from xlrd1 import open_workbook

# Create your views here.

##def index(request):
##  return render_to_response('client/index.html', {'message': 'Hello'})

class View_StoreSample(BaseHandler):
  def get(self):
    store = SampleStorage(args=json.dumps(self.request.args.lists()))
    store.put()

    return render_to_response('client/index.html', {'message': 'Sample stored.'})

store_sample = View_StoreSample()

##def store_sample(request):
##  store = SampleStorage(args=json.dumps(request.args.lists()))
##  store.put()
##
##  return render_to_response('client/index.html', {'message': 'Sample stored.'})
##
##
##class XLSFileUploadForm(forms.Form):
##  in_xls_file = forms.FileField(required=True)
##
##class XLSFileUpload(BaseHandler):
##  def prepare(self):
##    logging.debug('XLSFileUpload.prepare')
##
##  def get(self):
##    logging.debug('XLSFileUpload.get')
##
##    xls_upload_form = XLSFileUploadForm()
##
##    return render_to_response('client/xls_file_upload.html', {'form': xls_upload_form.as_widget(), 'token': 'notoken' })
##
##  def post(self):
##    logging.debug('XLSFileUpload.post')
##
##    xls_upload_form = XLSFileUploadForm()
##
##    if xls_upload_form.validate(self.request.form, self.request.files):
##      logging.debug('process data here')
##
##      in_data = [ ]
##
##      for i in self.request.files:
##        self.request.files[i].stream.seek(0)
##        in_file = self.request.files[i].stream.getvalue()
##
##        in_xls = open_workbook(file_contents=in_file)
##
##        set_trace()
##
##      logging.debug('data processed')
##
##      return render_to_response('client/index.html', { 'message': "/thanks/" })
##    else:
##      logging.debug('form did not validate')
##      return render_to_response('client/index.html', { 'message': "oopsie!" })
##
##xls_file_upload = XLSFileUpload()