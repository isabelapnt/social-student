#-*- coding: utf-8 -*-

# Arquivo fabfile.py
from fabric.api import local
from os.path import exists


def migrations():
    local("./manage.py makemigrations")
    local("./manage.py migrate")


def run(port=8000):
    local("./manage.py runserver {port}".format(port=port))


def fix(name):
    local("./manage.py fix_{name}".format(name=name))


def config_db():
    migrations()
    local("./manage.py fix_rh")
    run()


def collect():
    # local("./manage.py collectstatic --noinput")
    local("./manage.py collectmedia --noinput")


def dev():
    flush()
    migrations()
    collect()
    fix("super_user")
    fix("unidade_curso")
    fix("tag")
    fix("servico")
    fix("usuarios")
    fix("post")
    run()

def prod():
    migrations()
    fix("rh")


def flush():
    local("./manage.py flush --noinput")

def shell():
    local("./manage.py shell_plus")


