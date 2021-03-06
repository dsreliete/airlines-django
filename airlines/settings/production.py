# -*- coding: utf-8 -*-
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'airlines-travel.herokuapp.com']

DB_URL = get_env_variable('DATABASE_URL')
db_from_env = dj_database_url.config(DB_URL)

DATABASES['default'].update(db_from_env)


