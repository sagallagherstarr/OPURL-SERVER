# -*- coding: utf-8 -*-
#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        client.views.View_TitleList_Grid.py
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

class View_TitleList_Grid(BaseHandler):
  def get(self):
    in_xls = self.request.session['in_grid']

    base_sheet = in_xls.sheet_by_index(0)
    tenrows = [ base_sheet.row_values(i) for i in range(10) ]

    return render_to_response('client/gridbase_params.html', { 'in_grid': tenrows })