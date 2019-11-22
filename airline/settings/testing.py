# -*- coding: utf-8 -*-
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}