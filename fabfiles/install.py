from fabric.api import cd, env, local, put, run, settings, sudo, task
from fabric.context_managers import prefix
from fabric.contrib.console import confirm

from fabfiles import fab_settings

@task()
def prepare_server():
    sudo("apt-get -y update")
    sudo("apt-get -y upgrade")
    sudo("apt-get -y install python-pip")
    sudo("apt-get -y install git")
    sudo("apt-get -y install gcc")

@task()
def install_webserver():
    sudo("apt-get -y install nginx")

@task()
def create_virtualenv():
    sudo("pip install virtualenv")
    run("virtualenv " + env.virtualenv_dir)

@task()
def install_appserver():
    sudo("apt-get -y install supervisor")
    with prefix(env.activate):
        run("pip install gunicorn")

@task()
def prepare_pip_PIL():
    '''
    Preparations for PIL
    see: http://jj.isgeek.net/2011/09/install-pil-with-jpeg-support-on-ubuntu-oneiric-64bits/
    Better to run this manually, see where the files for the symlinks have landed
    '''
    sudo("apt-get -y install libjpeg8 libjpeg8-dev libfreetype6 libfreetype6-dev zlib1g-dev")
    with settings(warn_only=True):
        sudo("ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib")
        sudo("ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib")
        sudo("ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib")

@task()
def install_public_project():
    with prefix(env.activate):
        run("pip install django-public-project")

@task()
def install_dev_requirements():
    with prefix(env.activate):
        run("pip install -r https://raw.github.com/holgerd77/django-public-project/master/requirements_dev.txt")
        
@task()
def install_postgres_as_db():
    sudo("apt-get -y install postgresql")
    sudo("apt-get -y install postgresql-server-dev-9.1")
    with prefix(env.activate):
        run("pip install psycopg2")
    run("sudo -u postgres psql -c \"ALTER USER postgres WITH PASSWORD '" + env.db_postgres_postgres_pwd + "';\"")
    sudo("adduser " + env.db_postgres_user)
    run("sudo -u postgres psql -c \"CREATE USER " + env.db_postgres_user + " WITH PASSWORD '" + env.db_postgres_user_pwd + "'\"")
    run('sudo -u postgres psql -c "CREATE DATABASE ' + env.db_postgres_user + ' WITH OWNER=' + env.db_postgres_user + '"')


@task()
def install_webserver_config():
    put('config-scripts/nginx/public-project', '/etc/nginx/sites-available/public-project', True)
    with settings(warn_only=True):
        sudo("ln -s /etc/nginx/sites-available/public-project /etc/nginx/sites-enabled/public-project")
    sudo("/etc/init.d/nginx reload")
    

@task(alias='uwsc')
def install_appserver_config():
    put('config-scripts/gunicorn/gunicorn-public-project.sh', '/etc/gunicorn-public-project.sh', True, False, mode=0755)
    put('config-scripts/gunicorn/supervisor/gunicorn-public-project.conf', '/etc/supervisor/conf.d/gunicorn-public-project.conf', True)
    sudo('supervisorctl reload')
