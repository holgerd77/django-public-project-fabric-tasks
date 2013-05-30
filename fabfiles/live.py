from fabric.api import env, sudo, task
from fabric.context_managers import prefix


@task()
def webserver(command):
    sudo("/etc/init.d/nginx " + command, pty=False)

@task()
def appserver(command):
    with prefix(env.activate):
        sudo('supervisorctl ' + command + " gunicorn-public-project", pty=False)