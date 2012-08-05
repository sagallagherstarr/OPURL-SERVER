# -*- coding: utf-8 -*-
#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        client.views.View_XLSFileUpload.py
# Purpose:
#
# Author:      scott
#
# Created:     30/07/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import logging
import json
import zipfile


from google.appengine.api import (
  users,
  memcache,
)

from werkzeug import (
  unescape,
  redirect,
  Response,
  datastructures,
)

from werkzeug.exceptions import (
  NotFound,
  MethodNotAllowed,
  BadRequest,
)

from kay.utils import (
  render_to_response,
  set_trace,
  reverse,
  get_by_key_name_or_404,
  get_by_id_or_404,
  to_utc,
  to_local_timezone,
  url_for,
  raise_on_dev,
  forms,
)

from kay.i18n import gettext as _
from kay.auth.decorators import login_required

from google.appengine.datastore.datastore_query import Cursor

from kay.utils.paginator import (
  Paginator,
)

from kay.handlers import (
  BaseHandler,
)

from client.forms import XLSFileUploadForm

from xlrd1 import open_workbook

# Create your views here.

class XLSFileUpload(BaseHandler):
  def prepare(self):
    logging.debug('XLSFileUpload.prepare')

  def get(self):
    logging.debug('XLSFileUpload.get')

    xls_upload_form = XLSFileUploadForm()

    return render_to_response('client/xls_file_upload.html', {'form': xls_upload_form.as_widget() })

  def post(self):
    logging.debug('XLSFileUpload.post')

    xls_upload_form = XLSFileUploadForm()

    if xls_upload_form.validate(self.request.form, self.request.files):
      logging.debug('process data here')

      in_data = [ ]

      for i in self.request.files:
        self.request.files[i].stream.seek(0)
        in_file = self.request.files[i].stream.getvalue()

        in_xls = open_workbook(file_contents=in_file)

##        base_sheet = in_xls.sheet_by_index(0)
##        tenrows = [ base_sheet.row_values(i) for i in range(10) ]
        request.session['in_xls'] = in_xls

      logging.debug('data processed')
      return redirect('/client/title_list_grid')

##      return render_to_response('client/one_message.html', { 'message': "/thanks/" })
##      return redirect('client/process_spreadsheet.html', { 'message': 'I care', 'sheet': in_xls})
    else:
      logging.debug('form did not validate')
      return render_to_response('client/one_message.html', { 'message': "oopsie!" })

xls_file_upload = XLSFileUpload()