# -*- coding: utf-8 -*-
# client.models.Model_OneRecord.py

#from google.appengine.ext import db
##import logging

from google.appengine.ext import ndb
# Create your models here.

class Model_OneRecord(ndb.Expando):
  input_filename = ndb.StringProperty() # yes, very redundant
  input_lineno = ndb.IntegerProperty()
  input_rawtext = ndb.TextProperty()