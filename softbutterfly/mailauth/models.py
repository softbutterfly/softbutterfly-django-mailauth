# -*- encoding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group as LegacyGroup
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
# from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            UnicodeUsernameValidator(),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        blank=True,
        null=True,
    )

    email = models.EmailField(
        _('email address'),
        unique=True,
        max_length=254,
        error_messages={
            'unique': "A user with that email address already exists.",
        },
    )

    first_name = models.CharField(
        _('first name'),
        max_length=32,
        blank=True
    )

    last_name = models.CharField(
        _('last name'),
        max_length=32,
        blank=True
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        )
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as '
            'active. Unselect this instead of deleting accounts.'
        )
    )

    date_joined = models.DateTimeField(
        _('date joined'),
        default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

        swappable = 'AUTH_USER_MODEL'

    """
    def get_absolute_url(self):
        return "/users/{0:}/".format(urlquote(self.email))
    """

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{0:} {0:}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def get_other_username(self):
        return self.username

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])


class Group(LegacyGroup):
    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')
        proxy = True
        app_label = 'mailauth'
