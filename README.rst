django-auth-wall
================

.. image:: https://pypip.in/v/django-auth-wall/badge.png
    :target: https://pypi.python.org/pypi/django-auth-wall
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/theskumar/django-auth-wall.svg
   :target: https://travis-ci.org/theskumar/django-auth-wall
   :alt: Latest Travis CI build status

A very basic Basic Auth middleware that uses a username/password defined in
your environment variable or settings.py to protect whole of your site.
Does not use Django auth.

Handy for quickly securing an entire site during development, for example.

**Note**:  Environment variables is preferred over ``settings.py``.

Usage
-----

.. code::python

    # In settings.py:

    MIDDLEWARE_CLASSES = (
        'django_auth_wall.middleware.BasicAuthMiddleware',

        # all other middleware here
    )

    # Optionally, set it here if not setting as environment variable
    # Requires both variable to be set, else site won't be protected.
    AUTH_WALL_USERNAME = 'user'
    AUTH_WALL_PASSWORD = 'pass'

    """

Installation
------------

.. code::python

    pip install django-auth-wall

**Warning**

Please make sure that you use SSL/TLS (HTTPS) to encrypt the connection between
the client and the server, when using basic access authentication. In basic
access authentication username and password are sent in cleartext, and if
SSL/TLS is not used, the credentials could be easily intercepted.

Compatibility
-------------
- Django 1.5+

Licence
-------

MIT

Authors
-------

`django-auth-wall` was written by `Saurabh Kumar <saurabh@saurabh-kumar.com>`_.
