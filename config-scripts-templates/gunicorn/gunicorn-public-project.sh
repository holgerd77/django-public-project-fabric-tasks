#!/bin/bash
set -e
source /path/to/your/virtualenv/bin/activate
exec gunicorn_django -b 127.0.0.1:8000 --settings=yourproject.settings --pythonpath=/path/to/your/djangoproject/ --workers=3