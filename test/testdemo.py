import django
import os
import rest_framework
from django.utils import timezone
import logging
import sys
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zlzserver.settings")
django.setup()


logger = logging.getLogger("django")


print("auth_from 123")
logger.debug("auth_from : %s", "123")
