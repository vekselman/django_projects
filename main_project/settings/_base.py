# _base.py for shared settings

import os
import sys
import json
from django.core.exceptions import ImproperlyConfigured
from main_project.apps.core.versioning import get_git_changeset_timestamp

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
# BASE_DIR == C:\Users\<USER>\PycharmProjects\django_projects
# In order to get current timestamp of git
timestamp = get_git_changeset_timestamp(BASE_DIR)
STATIC_URL = f'/static/{timestamp}/'

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
EXTERNAL_BASE = os.path.join(BASE_DIR, "externals")
EXTERNAL_LIBS_PATH = os.path.join(EXTERNAL_BASE, "libs")
EXTERNAL_APPS_PATH = os.path.join(EXTERNAL_BASE, "apps")

sys.path = ["", EXTERNAL_APPS_PATH, EXTERNAL_APPS_PATH] + sys.path

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
