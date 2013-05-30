import os
from fabric.api import env

#Fabric host settings to connect to server
#Change these settings depending on how you want to connect to your server (password, key file)
#see http://docs.fabfile.org/en/latest/usage/execution.html
env.hosts = ['username@myserver.de',]
env.key_filename = '~/.ssh/mykeyfile'


#Specific settings for django-public-project tasks
env.django_project_dir = '/path/to/your/djangoproject/' #Django project directory
env.virtualenv_dir = '/path/to/your/virtualenv/'        #Directory for virtualenv environment
env.db_postgres_postgres_pwd = ''                       #Password for Postgres user postgres
env.db_postgres_user = ''                               #Username/DB name for installation 
env.db_postgres_user_pwd = ''                           #Password of user for installation


#Static, do not change
env.activate = 'source ' + os.path.join(env.virtualenv_dir, 'bin/activate')