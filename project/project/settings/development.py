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

# TEST
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
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
