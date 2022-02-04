#!/bin/sh

echo "Starting migrations [EntryPoint]"

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate --settings=FitTracker.settings.base  || exit 1

echo "Finished migrations [EntryPoint]"
exec "$@"