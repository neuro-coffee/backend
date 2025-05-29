from django.contrib import admin
from django.contrib.auth.models import Group as BaseGroupModel

from apps.users import models

admin.site.unregister(BaseGroupModel)

admin.site.register(models.UserModel)
