#!/bin/bash
set -e
source /path/to/your/virtualenv/bin/activate
exec gunicorn yourproject.wsgi:application -b 127.0.0.1:8000 --settings=yourproject.settings --pythonpath=/path/to/your/djangoproject/ --workers=3