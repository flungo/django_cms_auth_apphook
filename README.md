Django CMS Auth Apphook
=======================

App hook to make integration with the standard Django Auth Library (`django.contrib.auth`) easier. Also includes templates for all auth views.

Installation
------------

To install, you will need to clone the git, then run the setup.py script:

    git clone https://github.com/flungo/django_cms_auth_apphook.git
    cd django_cms_auth_apphook
    python setup.py
  
Configuration
-------------

Add `auth_apphook` to your list of `INSTALLED_APPS`. It's position doesn't matter unless you have `django.contrib.admin` installed (which to be honest, you probably do) and you want to use the included templates. `django.contrib.admin` contains several templates for `django.contrib.auth` so in order to use the included templates (see bellow) you should make sure it is listed before `django.contrib.admin`.

    INSTALLED_APPS = (
        # ...
        'auth_apphook',
        # ...
        'django.contrib.auth',
        # ...
    )

Templates
---------------------

Included with this app are the core templates required by the front end to generate the appropriate pages. I have made them all extend "base.html" so they will by default have your theme but should you need to customise these, you can copy the `registration` directory to your templates directory and customise till your heart's content.
