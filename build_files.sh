#!/bin/bash

echo "Installing project dependencies..."
python3 -m pip3 install -r requirements.txt

echo "Performing database migrations..."
python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input

echo "Collecting static files..."
python3 manage.py collectstatic --no-input
