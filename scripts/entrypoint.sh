#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate
echo "TEST_FLAG variable set to '$TEST_FLAG'"
if [ "$TEST_FLAG" == "true" ]
then
    echo "Running tests"
    python manage.py test
else
    echo "Test flag set to false or unset, tests skipped"
fi


if [ "$LOCAL_SERV" == "true" ]
then
    echo "Local development server configuration detected, hosting on 'http://127.0.0.1:8000'"
    python manage.py runserver 0.0.0.0:8000
else
    echo "Production server configuration detected, hosting over port 80"
    uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
fi