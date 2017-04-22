# -*- encoding: utf-8 -*-
from django.apps import AppConfig

from .settings import APP_VERBOSE_NAME


class MailAuthConfig(AppConfig):
    name = 'softbutterfly.mailauth'
    verbose_name = APP_VERBOSE_NAME

    label = 'mailauth'
