#!/bin/bash

set -o errexit

python manage.py migrate --noinput

# python manage.py collectmedia --noinput

python manage.py flush --noinput
python manage.py fix_super_user 
python manage.py fix_unidade_curso 
python manage.py fix_tag 
python manage.py fix_servico 
python manage.py fix_usuarios 
python manage.py fix_post 

