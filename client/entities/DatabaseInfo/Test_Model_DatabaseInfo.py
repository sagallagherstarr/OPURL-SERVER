#-------------------------------------------------------------------------------
# Name:        test.Test_Model_DatabaseInfo
# Purpose:
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

db1 = {
  'long_name': 'Academic Search Premier',
  'short_name': 'aph',
  'title_list_url': [
    'http://ebscohost.com/titleLists/aph-journals.xls',
    'http://ebscohost.com/titleLists/aph-other.xls',
    'http://ebscohost.com/titleLists/aph-journals.xls',
   ]
}

class Test_Model_DatabaseInfo(GAETestBase):
  CLEANUP_USED_KIND = True
  USE_PRODUCTION_STUBS = True

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_1(self):
    pass

  def test_2(self):
    pass
