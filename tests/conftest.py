import django
from django.conf import settings

try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello")


urlpatterns = [url(r"^$", index)]


def pytest_configure():
    settings.configure(
        DEBUG=True,
        SECRET_KEY="super_secret",
        ROOT_URLCONF=__name__,
        MIDDLEWARE_CLASSES=["django_auth_wall.middleware.BasicAuthMiddleware"],
    )
    django.setup()
