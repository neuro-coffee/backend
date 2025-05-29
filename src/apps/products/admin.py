from django.contrib import admin

from apps.products import models

admin.site.register(models.ProductModel)
admin.site.register(models.ProductTypeModel)
admin.site.register(models.PromoModel)
admin.site.register(models.PromoConditionModel)
admin.site.register(models.BasketModel)
