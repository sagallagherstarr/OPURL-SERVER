#-------------------------------------------------------------------------------
# Name:        forms.XLSFileUploadForm
# Purpose:
#
# Author:      scott
#
# Created:     30/07/2012
# Copyright:   (c) scott 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


##import logging
##import json
##import zipfile

from kay.utils import forms

class XLSFileUploadForm(forms.Form):
  in_xls_file = forms.FileField(required=True)