#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python3 manage.py collectstatic --no-input

# Crée les fichiers de migration si nécessaire
python3 manage.py makemigrations  --no-input

# Applique toutes les migrations
# python3 manage.py migrate --fake-initial  --no-input
# python3 manage.py migrate core zero --no-input
python3 manage.py migrate --no-input