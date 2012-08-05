#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        client.entities.TitleListInfo.tests
# Purpose:     unit tests for TitleListInfo entity
#
# Author:      scott
#
# Created:     30/07/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from google.appengine.ext import db
from werkzeug import BaseResponse, Client, Request
from kay.app import get_application
from kay.utils.test import (
  init_recording, get_last_context, get_last_template, disable_recording,
)
from kay.ext.testutils.gae_test_base import GAETestBase

from .models import TitleListInfo

class test_TitleListInfo(GAETestBase):
  CLEANUP_USED_KIND = True
  USE_PRODUCTION_STUBS = True

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_1(self):
    self.fail('test_TitleListInfo.test_1 not written')

##  def test_2(self):
##    pass
