# -*- coding: utf-8 -*-
# client.entities.ColumnTypes.tests

#-------------------------------------------------------------------------------
# Name:        ColumnTypes.tests
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

from google.appengine.ext import db
from werkzeug import BaseResponse, Client, Request
from kay.app import get_application
from kay.utils.test import (
  init_recording, get_last_context, get_last_template, disable_recording,
)
from kay.ext.testutils.gae_test_base import GAETestBase

from .models import (
  ColumnTypes,
  initial_columns,
)

from client.entities.VendorInfo.models import VendorInfo

def populate_ColumnTypes_from_initial():
  """populate_ColumnTypes_from_initial makes the assumption that there are
     currently no ColumnTypes in the datastore.  It uses the initial_columns
     data to re-populate from the default list.

     No inputs.
     No outputs.
     Changes the datastore.
  """

  vendors = { }

  # First, pick up all of the vendor names so we can look up keys.
  for i in initial_columns:
    for v in i['vendor_labels']:
      vendors[v] = None

  for i in vendors:
    vendors[i] = VendorInfo.query(keys_only=True).filter(VendorInfo.vendor_name == i).get()

  # now, with a list of VendorInfo keys, we can start populating
  for i in initial_columns:
    c = ColumnTypes()
    c.display_label = i['display_label']
    c.type_code = i

    for j in i['vendor_labels']:
      c.labels.append(VendorLabels(vendor=vendors[j], column_labels=i['vendor_labels'][j]))

    c.put()

  # all done, just drop out again.

def remove_all_ColumnTypes_data(assent=False):
  """If the parameter assent is True, remove all ColumnTypes (usually preparatory

     Inputs: assent - must evaluate to True in order to remove all ColumnTypes
     No outputs.
     Changes the datastore.
  """

  if assent is True:
    all_columns = ColumnTypes.all(keys_only=True)
    ndb.delete_multi(all_columns)
