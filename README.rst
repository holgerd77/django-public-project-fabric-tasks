======================================
Fabric tasks for django-public-project
======================================

This repository contains tasks for ``Fabric`` (http://fabfile.org) to make it easier to setup, deploy
and run a ``django-public-project`` installation.

These tasks were written for having a following environment:

* Ubuntu as a server/linux system
* Python/Django/Libraries in a virtual environment with virtualenv
* Nginx as static server
* Gunicorn as application server

You can use the tasks as a guideline for what is needed to have a working installation, or you
can use them "as is" if you want to set up the same environment as described above.

You probably want to install this repository directly from GitHub with::

    git clone https://github.com/holgerd77/django-public-project-fabric-tasks.git

And update it from time to time with::

    git pull

You can get a list of available tasks with::

    fabric --list

Create a settings file ``fabfiles/fab_settings.py`` using the provided ``fabfiles/fab_settings_template.py``
file to get things up and running.
 

