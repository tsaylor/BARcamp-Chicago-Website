import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

sys.path.insert(0, '/var/django/barcamp-2010')
sys.path.insert(0, '/var/django/barcamp-2010/project')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
