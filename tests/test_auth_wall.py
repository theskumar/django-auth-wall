import base64
from django.test import SimpleTestCase
from django_auth_wall.middleware import BasicAuthMiddleware


def test_get_header():
    obj = BasicAuthMiddleware()
    assert obj.auth_header() == 'Basic realm="Development"'


class AuthWallTest(SimpleTestCase):

    def get_auth_header(self, username, password):
        token = base64.b64encode('{0}:{1}'.format(username, password))
        return {
            'HTTP_AUTHORIZATION': 'Basic ' + token,
        }

    def test_no_auth_required(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_auth_required(self):
        with self.settings(AUTH_WALL_USERNAME='abc',
                           AUTH_WALL_PASSWORD='abc'):
            response = self.client.get('/')
            assert response.status_code == 401

            response = self.client.get('/', **self.get_auth_header('abc', 'abc'))
            assert response.status_code == 200

            response = self.client.get('/', **self.get_auth_header('abc', 'abc2'))
            assert response.status_code == 401
