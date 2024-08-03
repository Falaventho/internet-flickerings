#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate
echo "Running tests"
python manage.py test

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi