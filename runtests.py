#!/usr/bin/env python

"""
This suite runs tests in django environment. See:
https://docs.djangoproject.com/en/1.11/topics/testing/advanced/#using-the-django-test-runner-to-test-reusable-applications
"""

import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    print('Django: ', django.VERSION)
    print('Python: ', sys.version)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.app.settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner(interactive=False, keepdb=False, parallel=0)
    failures = test_runner.run_tests(['plane'])
    sys.exit(bool(failures))
