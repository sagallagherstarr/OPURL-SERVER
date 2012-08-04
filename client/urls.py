# -*- coding: utf-8 -*-
# client.urls
# 

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='client.views.index'),
  )
]

