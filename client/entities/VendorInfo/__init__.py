#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        entities.VendorInfo.__init__
# Purpose:     Provide all of the models, forms, views and tests for the
#              VendorInfo entity.
#
# Author:      scott
#
# Created:     01/08/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

__all__ = [
  'VendorInfo',
  'test_VendorInfo',
  'add_database_to_vendor'
]

from .models import (
  VendorInfo,
)

from .tests import (
  test_VendorInfo,
)

from .lib import (
  add_database_to_vendor,
)

