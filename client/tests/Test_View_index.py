#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      scott
#
# Created:     01/08/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##from google.appengine.ext import db
from werkzeug import BaseResponse, Client, Request
from kay.app import get_application
from kay.utils.test import (
  init_recording, get_last_context, get_last_template, disable_recording,
)
from kay.ext.testutils.gae_test_base import GAETestBase

# from myapp.models import Comment

class test_View_index(GAETestBase):
  CLEANUP_USED_KIND = True
  USE_PRODUCTION_STUBS = True

  def setUp(self):
    init_recording()
    app = get_application()
    self.client = Client(app, BaseResponse)

  def tearDown(self):
    disable_recording()

  def test_base(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 404)

  def test_client_get(self):
    response = self.client.get('/client')
    self.assertEquals(response.status_code, 301)

  def test_client_head(self):
    self.fail('test_View_index.test_client_head not yet written')

  def test_client_post(self):
    self.fail('test_View_index.test_client_post not yet written')

  def test_client_put(self):
    self.fail('test_View_index.test_client_put not yet written')

  def test_client_delete(self):
    self.fail('test_View_index.test_client_delete not yet written')

  def test_client_options(self):
    self.fail('test_View_index.test_client_options not yet written')

  def test_client_trace(self):
    self.fail('test_View_index.test_client_trace not yet written')

  def test_client_connect(self):
    self.fail('test_View_index.test_client_connect not yet written')

