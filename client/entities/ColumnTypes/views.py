# -*- coding: utf-8 -*-
# client.entities.ColumnTypes.views

#-------------------------------------------------------------------------------
# Name:        ColumnTypes.views
# Purpose:     provide a model and associated services for assigning data
#              types to spreadsheet columns for import.
#
# Author:      scott
#
# Created:     30/07/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

"""This view module gives us a way to reset the list of column types and
associated vendor data to a known default, deleting all of the other entered
data.  The administrator will need to verify that this is really, truly the desired
action before anything is done.  This is a hard reset
"""

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

class ColumnTypes_Reset(BaseHandler):
  def get(self):
    pass

  def post(self):
    pass