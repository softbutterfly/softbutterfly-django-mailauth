from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as LegacyGroupAdmin
from django.contrib.auth.admin import UserAdmin as LegacyUserAdmin
from django.contrib.auth.models import Group as LegacyGroup
from django.utils.translation import ugettext_lazy as _

from .forms import UserChangeForm
from .forms import UserCreationForm
from .models import User
from .models import Group
from .settings import REGISTER_PROXY_AUTH_GROUP_MODEL
from .settings import ENABLE_USERNAME


@admin.register(User)
class UserAdmin(LegacyUserAdmin):
    fieldsets = (
        (
            None, {
                'fields': (
                    'email',
                    'username',
                    'password',
                ) if ENABLE_USERNAME else (
                    'email',
                    'password',
                )
            }
        ),
        (
            _('Personal info'), {
                'fields': (
                    'first_name',
                    'last_name'
                )
            }
        ),
        (
            _('Permissions'), {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                )
            }
        ),
        (
            _('Important dates'), {
                'fields': (
                    'last_login',
                    'date_joined'
                )
            }
        ),
    )

    add_fieldsets = (
        (
            None, {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'email',
                    'password1',
                    'password2'
                ),
            }
        ),
    )

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        'email',
        'username',
        'first_name',
        'last_name',
        'is_staff'
    ] if ENABLE_USERNAME else [
        'email',
        'first_name',
        'last_name',
        'is_staff'
    ]

    search_fields = [
        'email',
        'username',
        'first_name',
        'last_name',
    ] if ENABLE_USERNAME else [
        'email',
        'first_name',
        'last_name',
    ]

    readonly_fields = [
        'last_login',
        'date_joined',
    ]

    ordering = [
        'email',
    ]


if REGISTER_PROXY_AUTH_GROUP_MODEL:
    admin.site.unregister(LegacyGroup)

    @admin.register(Group)
    class GroupAdmin(LegacyGroupAdmin):
        pass
