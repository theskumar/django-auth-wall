# django-auth-wall

[![Latest PyPI version](https://img.shields.io/pypi/v/django-auth-wall.svg)](https://pypi.python.org/pypi/django-auth-wall)

A very basic Basic Auth middleware that uses a username/password defined
in your environment variable or settings.py to protect whole of your
site. Does not use Django auth.

Handy for quickly securing an entire site during development, for
example.

**Note**: Environment variables is preferred over `settings.py`.

# Usage

```
# In settings.py:

MIDDLEWARE = [
    'django_auth_wall.middleware.BasicAuthMiddleware',

    # all other middleware here
]

# Optionally, set it here if not setting as environment variable
# Requires both variable to be set, else site won't be protected.
AUTH_WALL_USERNAME = 'user'
AUTH_WALL_PASSWORD = 'pass'
```

# Installation


```shell
pip install django-auth-wall
```

**Warning**

Please make sure that you use SSL/TLS (HTTPS) to encrypt the connection
between the client and the server, when using basic access
authentication. In basic access authentication username and password are
sent in cleartext, and if SSL/TLS is not used, the credentials could be
easily intercepted.

# Compatibility

-   Django 1.5+

# Licence

MIT

# Authors

[django-auth-wall] was written by [Saurabh Kumar](https://github.com/theskumar).
