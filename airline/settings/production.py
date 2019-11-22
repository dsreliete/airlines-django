# -*- coding: utf-8 -*-
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['django-airlines.heroku.com']

DB_URL = get_env_variable('DATABASE_URL')
db_from_env = dj_database_url.config(DB_URL)
DATABASES['default'].update(db_from_env)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}