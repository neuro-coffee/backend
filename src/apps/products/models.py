from django.db import models


class ProductModel(models.Model):
    name = models.CharField('название', db_index=True, max_length=255)
    description = models.TextField('описание', blank=True)
    image = models.ImageField('изображение', upload_to='products/')
    price = models.FloatField('цена')
    weight = models.FloatField('вес', blank=True, null=True)
    calorific = models.FloatField(
        'калорийность',
        blank=True,
        null=True,
        help_text='измеряется в ккал',
    )
    types = models.ManyToManyField(
        'ProductTypeModel',
        verbose_name='',
        related_name='products',
        blank=True,
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class ProductTypeModel(models.Model):
    name = models.CharField('название', db_index=True, max_length=255)

    class Meta:
        verbose_name = 'тип товаров'
        verbose_name_plural = 'типы товаров'


class PromoModel(models.Model):
    name = models.CharField('название', max_length=255)
    short_description = models.TextField('краткое описание')
    description = models.TextField('описание')

    class Meta:
        verbose_name = 'акция'
        verbose_name_plural = 'акции'


class PromoConditionModel(models.Model):
    description = models.TextField('описание')
    promo = models.ForeignKey(
        PromoModel,
        verbose_name='акция',
        related_name='conditions',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'условие акции'
        verbose_name_plural = 'условия акции'


class BasketModel(models.Model):
    products = models.ManyToManyField(
        ProductModel,
        verbose_name='корзина',
        related_name='baskets',
        blank=True,
    )

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
