from django.contrib import admin

from apps.products import models

admin.site.register(models.ProductModel)
admin.site.register(models.ProductTypeModel)
admin.site.register(models.BasketModel)


class PromoConditionInLine(admin.TabularInline):
    model = models.PromoConditionModel
    extra = 0


@admin.register(models.PromoModel)
class PromoModelAdmin(admin.ModelAdmin):
    inlines = [PromoConditionInLine]
