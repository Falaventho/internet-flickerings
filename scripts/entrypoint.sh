#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

if [ "$TEST" == "true"]
then
    echo "Running tests"
    python manage.py test
else
    echo "Tests skipped"
fi

python manage.py runserver 0.0.0.0:8000