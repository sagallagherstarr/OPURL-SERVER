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
  initial_columns, # also makes good test data
)

from client.entities.VendorInfo.models import VendorInfo

class test_ColumnTypes(GAETestBase):
  CLEANUP_USED_KIND = True
  USE_PRODUCTION_STUBS = True

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_1(self):
    self.fail('test_ColumnTypes.test_1 not written')