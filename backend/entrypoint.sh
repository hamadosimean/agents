#!/bin/sh

set -e  

echo "Running migrations..."

python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Server..."
exec gunicorn -b 0.0.0.0:8000 --workers 3 --timeout 300 config.wsgi:application
