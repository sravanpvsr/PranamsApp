# Reference copy of the PythonAnywhere WSGI file.
#
# PythonAnywhere does NOT read this file. The live one is
#   /var/www/pranams_pythonanywhere_com_wsgi.py
# (Web tab -> "WSGI configuration file"). Replace its whole contents with
# the code below. See DEPLOY.md.
#
# Settings read SECRET_KEY, DEBUG etc. from /home/pranams/PranamsApp/.env,
# so nothing secret belongs in this file.

import os
import sys

PROJECT_DIR = '/home/pranams/PranamsApp'
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoAPI.settings'

from django.core.wsgi import get_wsgi_application  # noqa: E402

application = get_wsgi_application()
