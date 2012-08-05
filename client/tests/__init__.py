#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        client.tests.__init__
# Purpose:     Import all test cases from various places, to make them available
#              for unit testing
#
# Author:      scott
#
# Created:     01/08/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__all__ = [
# from Test_View_index
  'test_View_index',
# from client.entities
  'test_DatabaseInfo',
  'test_TitleListInfo',
  'test_TitleRecord',
  'test_VendorInfo',
]

from .Test_View_index import test_View_index

from client.entities.DatabaseInfo.tests import test_DatabaseInfo
from client.entities.TitleListInfo.tests import test_TitleListInfo
from client.entities.TitleRecord.tests import test_TitleRecord
from client.entities.VendorInfo import test_VendorInfo