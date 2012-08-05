#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        TitleRecord
# Purpose:     holds information about individual titles in a title list
#
# Author:      scott
#
# Created:     01/08/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from google.appengine.ext import ndb
from google.appengine.api.logservice import logservice

from client.entities.DatabaseInfo import DatabaseInfo
from client.entities.ColumnTypes import ColumnTypes

class ColumnRecord(ndb.Model):
  """Not a standalone model, but a StructuredProperty for TitleRecord
  """
  column_type = ndb.KeyRecord(kind=ColumnTypes)
  column_value = ndb.StringProperty()

class TitleRecord(ndb.Model):
  """Hold information about one title in the database, regardless of which
     database(s) it appears in.
     Use ColumnTypes references to keep vendor labeling straight
  """

  database_info = ndb.KeyProperty(kind=DatabaseInfo, repeated=True)
  column_data = ndb.StructuredProperty(ColumnRecord, repeated=True)

  @classmethod
  def _construct_standard_number_search(cls, in_standard_number):
    return cls.query(ndb.AND(TitleRecord.column_data.column_type == 'standard_number',
                                     TitleRecord.column_data.column_value == in_standard_number
                                    )
                            )

  @classmethod
  def _construct_title_search(cls, in_standard_number):
    return cls.query(ndb.AND(TitleRecord.column_data.column_type == 'publication_name',
                                     TitleRecord.column_data.column_value == in_title
                                    )
                            )
  @classmethod
  def find_by_standard_number(cls, in_standard_number):
    return cls._construct_standard_number_search(in_standard_number).get() # there can be only one, right?

  @classmethod
  def find_by_title(in_title):
    return cls._construct_title_search(in_title).get() # there can be only one, right?

  @classmethod
  def find_by_standard_number_or_title(cls, in_standard_number=None, in_title=None):
    if (in_standard_number is None) and (in_title is None):
      raise BadValueError('empty standard number and title for search')

  return TitleRecord.query(ndb.OR(cls._construct_standard_number_search(in_standard_number),
                                  cls._construct_title_search(in_title)
                                 )
                          ).get() # there can still be only one, right?


