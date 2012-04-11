from . import *
import os
import sys


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_ROOT = BASE_PATH + '/media/'
STATIC_ROOT = BASE_PATH + '/static/'

# TEST
TEST_DISCOVERY_ROOT = os.path.join(BASE_PATH, "tests")
TEST_RUNNER = "tests.runner.DiscoveryRunner"

if 'test' in sys.argv:
    SOUTH_TESTS_MIGRATE = False
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
                },
            }
