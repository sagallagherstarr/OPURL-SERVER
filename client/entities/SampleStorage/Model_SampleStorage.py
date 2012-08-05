# -*- coding: utf-8 -*-
# client.models.Model_SampleStorage

#from google.appengine.ext import db
##import logging

from google.appengine.ext import ndb
# Create your models here.

##from lib.openpyxl import load_workbook

class Model_SampleStorage(ndb.Model):
  args = ndb.TextProperty()

##class OneRecord(ndb.Expando):
##  input_filename = ndb.StringProperty() # yes, very redundant
##  input_lineno = ndb.IntegerProperty()
##  input_rawtext = ndb.TextProperty()
##
##
##
