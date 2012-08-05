#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        models.Model_VendorInfo
# Purpose:
#
# Author:      scott
#
# Created:     30/07/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from google.appengine.ext.db import BadArgumentError, BadValueError, NotSavedError
from google.appengine.ext import ndb

from client.entities.DatabaseInfo import DatabaseInfo

class VendorInfo(ndb.Model):
  vendor_name = ndb.StringProperty(indexed=True, required=True)
  vendor_corporate_url = ndb.StringProperty()

  # We need to have the keys associated with these databases, so that individual
  # title records can be linked to their source databases
  databases = ndb.KeyProperty(kind=DatabaseInfo, repeated=True)