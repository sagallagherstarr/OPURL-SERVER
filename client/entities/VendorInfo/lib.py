#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        client.entities.VendorInfo.lib
# Purpose:     support function for the VendorInfo entity
#
# Author:      scott
#
# Created:     01/08/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from .models import (
  VendorInfo,
)

def add_database_to_vendor(vendor, database=None):
  vk = None
  dk = None

  if isinstance(vendor, VendorInfo):
    vk = vendor.key()

    if vk is None:
      vk = vendor.put()
  elif isinstance(vendor, basestring):
    vf = VendorInfo.query(VendorInfo.vendor_name == vendor).filter_deleted().get()

    if vf is not None:
      vk = vf.key()
      vendor = vf
    else:
      raise BadArgumentError('The name "%s" is not a current vendor', vendor)

  if database is not None:
    if not isinstance(database, (ndb.Key, DatabaseInfo)):
      raise BadValueError('The database information "%r" is not valid', database)
    else:
      if isinstance(database, ndb.Key):
        dk = database
      else:
        dk = database.key()

      if dk is None:
        database.put()
        dk = database.key()

      if dk is None:
        raise NotSavedError('Unable to reference database information "%r" in the datastore', database)

      vendor.database.append(dk)
      vendor.put()
