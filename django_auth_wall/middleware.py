from __future__ import unicode_literals

import base64
import os

from django.conf import settings
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import ugettext_lazy as _


from django_auth_wall import HTTP_HEADER_ENCODING


def get_env_or_settings(key, default=None):
    return os.environ.get(key, getattr(settings, key, default))


def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.
    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, type('')):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


class BasicAuthMiddleware(MiddlewareMixin):
    """
    A very basic Basic Auth middleware that uses a username/password defined in
    your environment variable or settings.py as AUTH_WALL_USERNAME and AUTH_WALL_PASSWORD.
    Does not use Django auth.

    Handy for quickly securing an entire site during development, for example.

    In settings.py:

    AUTH_WALL_USERNAME = 'user'
    AUTH_WALL_PASSWORD = 'pass'

    MIDDLEWARE_CLASSES = (
        'django_auth_wall.middleware.BasicAuthMiddleware',
        # All other middleware
    )
    """
    def process_request(self, request):
        AUTH_WALL_USERNAME = get_env_or_settings('AUTH_WALL_USERNAME')
        AUTH_WALL_PASSWORD = get_env_or_settings('AUTH_WALL_PASSWORD')

        if not (AUTH_WALL_USERNAME and AUTH_WALL_PASSWORD):
            return None

        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'basic':
            return self.unauthorized_response(request)

        try:
            auth_parts = base64.b64decode(auth[1]).decode(HTTP_HEADER_ENCODING).partition(':')
        except (TypeError, UnicodeDecodeError):
            msg = _('Invalid basic header. Credentials not correctly base64 encoded.')
            raise Exception(msg)
        username, password = auth_parts[0], auth_parts[2]

        if username == AUTH_WALL_USERNAME and password == AUTH_WALL_PASSWORD:
            return None

        return self.unauthorized_response(request)

    def unauthorized_response(self, request):
        response = HttpResponse("""<html><title>Authorization Required</title><body>
                                <h1>Authorization Required</h1></body></html>""")
        response['WWW-Authenticate'] = self.authenticate_header()
        response.status_code = 401
        return response

    def authenticate_header(self):
        www_authenticate_realm = get_env_or_settings('AUTH_WALL_REALM', "Development")
        return 'Basic realm="%s"' % www_authenticate_realm
