# -*- coding: utf-8 -*-
from .base import *

import django_heroku

DEBUG = False
ALLOWED_HOSTS = ['airlines-django.herokuapp.com']

django_heroku.settings(locals())