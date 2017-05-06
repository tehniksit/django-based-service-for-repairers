import sys

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

path = '/home/tehniksit/untitled2'

if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled2.settings")

application = StaticFilesHandler(get_wsgi_application())