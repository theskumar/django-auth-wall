from __future__ import unicode_literals

import base64

from django.test import SimpleTestCase
from django_auth_wall.middleware import BasicAuthMiddleware
from django_auth_wall import HTTP_HEADER_ENCODING


def test_get_header():
    def dummy_get_response(request):
        return None

    obj = BasicAuthMiddleware(dummy_get_response)
    assert obj.authenticate_header() == 'Basic realm="Development"'


class AuthWallTest(SimpleTestCase):
    def get_auth_header(self, username, password):
        token = base64.b64encode(
            ":".join([username, password]).encode(HTTP_HEADER_ENCODING)
        )
        return {
            "HTTP_AUTHORIZATION": b"Basic " + token,
        }

    def test_no_auth_required(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_auth_required(self):
        with self.settings(
            AUTH_WALL_USERNAME="abc",
            AUTH_WALL_PASSWORD="abc",
            MIDDLEWARE=["django_auth_wall.middleware.BasicAuthMiddleware"],
        ):
            response = self.client.get("/")
            assert response.status_code == 401

            response = self.client.get("/", **self.get_auth_header("abc", "abc"))
            assert response.status_code == 200

            response = self.client.get("/", **self.get_auth_header("abc", "abc2"))
            assert response.status_code == 401
