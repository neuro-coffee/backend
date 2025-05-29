from django.db import models

from django.contrib.auth.models import AbstractUser

from apps.users import consts


class UserModel(AbstractUser):
    last_name = models.CharField('фамилия', max_length=255)
    patronymic = models.CharField('отчество', max_length=255, blank=True)
    gender = models.CharField('пол', choices=consts.UserConsts.get_choices(), max_length=255)
    phone = models.CharField('телефон', max_length=255, blank=True)
    basket = models.OneToOneField(
        'products.BasketModel',
        verbose_name='корзина',
        related_name='user',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
