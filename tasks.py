from invoke import task
import subprocess

@task
def start(c):
    subprocess.Popen("npm run watch", shell=True)
    subprocess.Popen("cd deep_learning && python manage.py runserver", shell=True)