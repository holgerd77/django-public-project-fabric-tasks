#!/bin/bash
set -e
source /path/to/your/virtualenv/bin/activate

exec python manage.py celeryd