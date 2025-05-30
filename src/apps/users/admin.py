from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group as BaseGroupModel

from apps.users import models

admin.site.unregister(BaseGroupModel)


@admin.register(models.UserModel)
class UserModelAdmin(UserAdmin):
    pass
