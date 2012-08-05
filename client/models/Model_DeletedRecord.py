#-------------------------------------------------------------------------------
# Name:        models.Model_DeletedRecord
# Purpose:     Allows the user to delete any of our common datastore record types,
#              and allows for an undo facility.
#
# Author:      scott
#
# Created:     30/07/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from datetime import datetime

from google.appengine.ext import ndb

class Model_DeletedRecord(ndb.Model):
  deleted = ndb.BooleanProperty(default=False)
  deleted_by = ndb.UserProperty()
  deleted_on = ndb.DateTimeProperty(auto_now=True)

  def delete_record(self, by_user):
    self.deleted = True
    self.deleted_by = by_user
    self.deleted_on = datetime.now()
    self.put()

  @classmethod
  def filter_deleted(cls, query):
    return query.filter(cls.deleted == False)

class Model_PublicFace(ndb.Model):
  pass

states = [ 'create', 'modify', 'delete', 'undo' ]
# undo allows us to bring a previously buried modification to the front again

class Model_ModificationRecord(ndb.Model):
  modification = StructuredProperty(Model_Modifications)
  value = StructuredProperty(Model_PublicFace)

  state = ndb.StringProperty(choices=states)
  user = ndb.UserProperty(indexed=True)
  action_at = ndb.DateTimeProperty(indexed=True)

class Model_MainRecord(ndb.Model):
  publicface_name = ndb.StringProperty(indexed=True) # the name of the model class, a child of
  # Model_PublicFace

  publicface_model = ndb.StructuredProperty(Model_ModificationRecord, repeated=True)
  current_publicface_model = ndb.IntegerProperty(default=0) # for undo/redo

  @classmethod
  def create(cls, user, **entity_values):
    if not isinstance(publicface_model, (None, [ ])):
      pass # raise an invalid action error

    # create a new entity of our public-facing type
    # create a new entity of Model_ModificationRecord type, with the new entity
    # as a child and the modifcation being 'create'
    # push the new Model_ModificationRecord onto the front of our list of records

  def delete(self):
    # create a new Model_ModificationRecord as a delete record, with no public facing record
    # and stick that into the front of our list of records
    pass

  def get_publicface(self):
    # one, if our top entry is a deleted record, return None
    # two, return the public-facing member of the front of our list of records
    pass

  def update_publicface(self, **entity_values):
    # just create a new public-facing record, create an update record for that, and
    # stick that on the front of our list of records
    pass

  def get_history(self):
    # return the complete list of modifications available
    pass

  def undo_one_action(self):
    pass # dig back to one layer previous in the list of records

  def redo_one_action(self):
    pass # undoes an undo

  def flatten_history(self, list_len=10):
    pass # removes cruft from the list of records; preserves the last list_len records.

