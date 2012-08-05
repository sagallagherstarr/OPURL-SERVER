#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        client.entities.VendorInfo.form
# Purpose:     provide needed forms for VendorInfo user interface
#
# Author:      scott
#
# Created:     30/07/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from kay.utils import forms
from kay.utils.forms.modelform import ModelForm

from .models import VendorInfo

class Form_VendorInfo(ModelForm):
  class Meta:
    model = VendorInfo

