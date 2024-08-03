#!/bin/sh

set -e


if ["$TEST_FLAG" == "true" ]; then
    echo "Running tests"
    python manage.py test
else
    echo "Test flag set to '$TEST_FLAG', skipping tests"
fi

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi