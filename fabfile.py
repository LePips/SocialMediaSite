import os

from fabric.api import local, task
from fabric.decorators import runs_once

BASE_DIR = os.path.sep.join((os.path.dirname(__file__), ''))



@task
@runs_once
def start():
    """
    Runs the local Django server 8080
    """
    local('open "http://127.0.0.1:8080/" && python ./manage.py runserver 8080')

@task
@runs_once
def startad():
    """
    Runs server at the admin page
    """
    local('open "http://127.0.0.1:8080/admin" && python ./manage.py runserver 8080')

@task
@runs_once
def delpyc():
    """
    Runs the local Django server
    """
    local('find . -name "*.pyc" -delete')

@task
@runs_once
def shell():
    """
    Opens a Django shell on the target environment.
    """
    local('python manage.py shell')

@task
@runs_once
def provision():
    """
    Runs the local Django server
    """
    local("pip install -r requirements.txt")

@task
@runs_once
def syncdb():
    """
    Runs the local Django server
    """
    local("python manage.py syncdb")

@task
@runs_once
def makemigrations():
    """
    Makes Django migrations
    """
    local("python manage.py makemigrations")

@task
@runs_once
def migrate():
    """
    Makes Django migration
    """
    local("python manage.py migrate")
