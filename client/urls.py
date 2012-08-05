# -*- coding: utf-8 -*-
# client.urls
#

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='client.views.index'),
    Rule('/sample', endpoint='store_sample', view='client.views.store_sample'),
    Rule('/upload/local/xls', endpoint='xls_file_upload', view='client.views.xls_file_upload'),
  )
]

