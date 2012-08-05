#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        TitleListInfo
# Purpose:     holds information about a title list belonging to a database
#
# Author:      scott
#
# Created:     30/07/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from google.appengine.ext import ndb

class TitleListInfo(ndb.Model):
  title_list_url = ndb.StringProperty(verbose_name="URL For Title List")
  first_load_datetime = ndb.DateTimeProperty(auto_now_add=True, verbose_name="First Loaded")
  most_recent_load_datetime = ndb.DateTimeProperty(auto_now=True, verbose_name="Most Recently Loaded")

  active_bool = ndb.BooleanProperty(verbose_name="Active")
  deleted_bool = ndb.BooleanProperty(verbose_name="Deleted")