# _base.py for shared settings

import os
import json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
# BASE_DIR == C:\Users\<USER>\PycharmProjects\django_projects

TEMPLATES = [{
    "DIRS": [
        os.path.join(BASE_DIR, "main_project", "templates")
    ]
}]

LOCAL_PATHS = [
    os.path.join(BASE_DIR, "locale")
]

STATICFILES_DIRS =[
    os.path.join(BASE_DIR, "main_project", "site_static")
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
EXTERNALS_ROOT = os.path.join(BASE_DIR, "externals")


with open(os.path.join(BASE_DIR, "secrets", 'secrets.json'), 'r') \
        as f:
    secrets = json.loads(f.read())


def get_secret(settings):
    # To read sensitive settings from the environment variables
    """Get the secret variable or return explicit exception."""
    try:
        return os.environ[settings]
    except KeyError:
        error_msg = f'Set the {settings} environment variable'
        raise ImproperlyConfigured(error_msg)
##########################################################
# print(BASE_DIR)