# -*- coding: utf-8 -*-
from .base import *

DEBUG = True
ALLOWED_HOSTS = []

if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}