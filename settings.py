# -*- coding: utf-8 -*-

"""
A sample of kay settings.

:Copyright: (c) 2009 Accense Technology, Inc.
                     Takashi Matsuo <tmatsuo@candit.jp>,
                     All rights reserved.
:license: BSD, see LICENSE for more details.
"""

import os, os.path

DEFAULT_TIMEZONE = 'Americas/Los_Angeles'
DEBUG = True
PROFILE = False
SECRET_KEY = 'Sku^^pe7Y%%ar(secretts&trngi'
SESSION_PREFIX = 'gaesess:'
COOKIE_AGE = 1209600 # 2 weeks
COOKIE_NAME = 'KAY_SESSION'

ADMINS = (
)

TEMPLATE_DIRS = (
  'templates',
##  'media/html',
##  'media/templates',
##  'client/templates',
)

USE_I18N = False
DEFAULT_LANG = 'en'

SESSION_STORE = 'kay.sessions.sessionstore.GAESessionStore'
AUTH_USER_MODEL = 'kay.auth.models.GoogleUser'

INSTALLED_APPS = (
  'kay.sessions',
  'kay.auth',
  'client',
)

APP_MOUNT_POINTS = {
}

# You can remove following settings if unnecessary.
CONTEXT_PROCESSORS = (
  'kay.context_processors.request',
  'kay.context_processors.url_functions',
  'kay.context_processors.media_url',
)

MIDDLEWARE_CLASSES = (
  'kay.sessions.middleware.SessionMiddleware',
  'kay.auth.middleware.AuthenticationMiddleware',
)
