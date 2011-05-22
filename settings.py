# Django settings for django_template project.
import os
import sys

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

sys.path.append(os.path.join(PROJECT_PATH, 'apps'))
sys.path.append(os.path.join(PROJECT_PATH, 'libraries'))

MEDIA_ROOT = PROJECT_PATH + '/media/'
MEDIA_URL = '/media/'


STATIC_ROOT = PROJECT_PATH + '/static/'
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_PATH + '/templates',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)
