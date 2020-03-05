# airlines-django

[![Build Status](https://travis-ci.org/dsreliete/airlines-django.svg?branch=master)](https://travis-ci.org/dsreliete/airlines-django)

Notice for future me:
* secrets.py file is in my drive credentials folder, inside airlines-django!

It is important to know that locally I have 3 virtual enviroments:
- airlines
- airlines-test
- airlines-prod

To activate just hit the command:
- workon airlines or airlines-test or airlines-prod
After that, install app requirements:
- pip install -r requirements/development.txt to install development dependencies  
- pip install -r requirements/testing.txt for testing dependencies
- pip install -r requirements/production.txt to run prod dependencies.

Commands to run the app:
- python manager.py runserver
- python manager.py tests

If I do not find these venvs:
To create and to deactivate virtualenv:
- mkvirtualenv --python=/usr/local/bin/python3 (venv's name)
- deactivate

Setting env variables DJANGO_SETTINGS_MODULE
Set a postactivate script that will set the DJANGO_SETTINGS_MODULE  variable just after activating the virtual environment:
- workon airlines or airlines-test or airlines-prod
cd $VIRTUAL_ENV/bin
Edit the postactivate file by adding:
- export DJANGO_SETTINGS_MODULE="airlines.settings.development" or "...production" or "...testing"
And so install requiremnets and run the app


