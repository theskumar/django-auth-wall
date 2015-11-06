import os

from django.conf import settings
from django.http import HttpResponse


def get_env_or_settings(key, default=None):
    return os.environ.get(key, getattr(settings, key, default))


class BasicAuthMiddleware(object):
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

    def unauthorized_response(self):

        response = HttpResponse("""<html><title>Authorization Required</title><body>
                                <h1>Authorization Required</h1></body></html>""")
        response['WWW-Authenticate'] = self.auth_header()
        response.status_code = 401
        return response

    def process_request(self, request):
        AUTH_WALL_USERNAME = get_env_or_settings('AUTH_WALL_USERNAME')
        AUTH_WALL_PASSWORD = get_env_or_settings('AUTH_WALL_PASSWORD')

        if not (AUTH_WALL_USERNAME and AUTH_WALL_PASSWORD):
            return None

        auth_header = request.META.get('HTTP_AUTHORIZATION', None)
        if not auth_header:
            return self.unauthorized_response()

        (authmeth, auth) = auth_header.split(' ', 1)
        if 'basic' != authmeth.lower():
            return self.unauthorized_response()
        auth = auth.strip().decode('base64')
        username, password = auth.split(':', 1)

        if username == AUTH_WALL_USERNAME and password == AUTH_WALL_PASSWORD:
            return None

        return self.unauthorized_response()

    def auth_header(self):
        AUTH_WALL_REALM = get_env_or_settings('AUTH_WALL_REALM', "Development")
        return 'Basic realm="{}"'.format(AUTH_WALL_REALM)
