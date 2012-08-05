# -*- coding: utf-8 -*-
# client.models.Model_SampleStorage

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

from client.entities.TitleListInfo import TitleListInfo

class DatabaseInfo(ndb.Model):
  database_long_name = ndb.StringProperty(indexed=True, required=True, verbose_name="Database Name")
  database_shortname = ndb.StringProperty(verbose_name="Database Short Name")

  database_title_lists = ndb.KeyProperty(kind=TitleListInfo, repeated=True)
  database_subject_lists = ndb.KeyProperty(kind=TitleListInfo, repeated=True)