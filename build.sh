#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

# Crée les fichiers de migration si nécessaire
python manage.py makemigrations --no-input

# Applique toutes les migrations
python manage.py migrate --no-input
