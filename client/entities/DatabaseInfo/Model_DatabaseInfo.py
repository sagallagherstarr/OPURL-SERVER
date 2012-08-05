#-------------------------------------------------------------------------------
# Name:        Model_DatabaseInfo
# Purpose:
#
# Author:      scott
#
# Created:     30/07/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from google.appengine.ext import ndb
from Model_DeletedRecord import Model_Deleted_Record

from Model_TitleListInfo import Model_TitleListInfo

class Model_DatabaseInfo(Model_DeletedRecord):
  database_long_name = ndb.StringProperty(indexed=True, required=True, verbose_name="Database Name")
  database_shortname = ndb.StringProperty(verbose_name="Database Short Name")

  database_title_lists = ndb.KeyProperty(kind=Model_TitleListInfo, repeated=True)
  database_subject_lists = ndb.KeyProperty(kind=Model_TitleListInfo, repeated=True)