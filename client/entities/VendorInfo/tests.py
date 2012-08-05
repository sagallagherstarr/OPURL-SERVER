#-------------------------------------------------------------------------------
# Name:        test.Test_VendorInfo
# Purpose:     test all aspects of the VendorInfo - Model, View and any utility functions
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

from .models import VendorInfo # local models, not client.models

class test_VendorInfo(GAETestBase):
  CLEANUP_USED_KIND = True
  USE_PRODUCTION_STUBS = True

  def setUp(self):
    self.t1 = {
               'vendor_name': 'Database Vendor #1',
               'corporate_url': 'http://www.dbvendor1.com/',
               'database': [ ] # at this point, we don't have any
               # vendor databases set up, so just load in an empty list
              }

    self.t2 = {
               'vendor_name': 'The Squiggle',
               'corporate_url': 'squiggle.com',
               'database': []
              }

  def tearDown(self):
    pass

  def model_test_1(self):
    """Test simple record creation, put it to the datastore, and then retrieve it
    and compare the retrieved values with the put values.  Very simple really.
    """

    # create a record and verify that it was created
    v1 = VendorInfo(vendor_name=self.t1['vendor_name'], # yes, I know I could just
                          corporate_url=self.t1['corporate_url'], # derefernce the dict
                          database=self.t1['database']) # to get the same effect,
                          # but this method allows for more explicit configuration.
    self.AssertIsNotNone(v1)

    # now put the record, and check the success of doing so
    k1 = v1.put() # this may raise an error, and if it does the test fails, as it should.
    self.AssertIsNotNone(k1)

    # now retrieve the record, and make sure it's the same record we put
    rv1 = k1.get()
    self.AssertEqual(rv1.vendor_name, self.t1['vendor_name'])
    self.AssertEqual(rv1.corporate_url, self.t1['corporate_url'])
    self.AssertEqual(rv1.databases, self.t1['databases'])


##  def test_2(self):
##    pass