# -*- encoding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


SOFTBUTTERFLY = getattr(settings, 'SOFTBUTTERFLY', None)
MAILAUTH = SOFTBUTTERFLY.get('MAILAUTH', {})

APP_VERBOSE_NAME = MAILAUTH.get('APP_VERBOSE_NAME', _("Authentication and Authorization"))
REGISTER_PROXY_AUTH_GROUP_MODEL = MAILAUTH.get('REGISTER_PROXY_AUTH_GROUP_MODEL', True)
ENABLE_USERNAME = MAILAUTH.get('ENABLE_USERNAME', True)
