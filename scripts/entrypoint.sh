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

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi