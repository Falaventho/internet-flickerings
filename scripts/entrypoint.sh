#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

if [ "$TEST" == "1"]
then
    echo "Running tests"
    python manage.py test
else
    echo "Tests skipped"
fi

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi