#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        views.__init__.py
# Purpose:     top-level views; imports everything that's needed
#
# Author:      scott
#
# Created:     30/07/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__all__ = [
# from View_index
  'index',
  'xls_file_upload',
]

from View_index import index
from View_XLSFileUpload import xls_file_upload