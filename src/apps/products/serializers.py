from rest_framework import serializers

from apps.products import models


class BaseProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductTypeModel
        fields = ('name',)


class ProductListSerializer(serializers.ModelSerializer):
    types = BaseProductTypeSerializer(many=True)

    class Meta:
        model = models.ProductModel
        fields = ('id', 'name', 'description', 'image', 'price', 'weight', 'calorific', 'types')


class ProductRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        fields = ('name', 'price', 'description', 'weight', 'calorific')


class MenuListSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True)

    class Meta:
        model = models.MenuModel
        fields = ('name', 'products')


class BasePromoConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PromoConditionModel
        fields = ('description',)


class PromoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PromoModel
        fields = ('id', 'name', 'short_description')


class PromoRetrieveSerializer(serializers.ModelSerializer):
    conditions = BasePromoConditionSerializer(many=True)

    class Meta:
        model = models.PromoModel
        fields = ('name', 'short_description', 'description', 'conditions')


class BasketBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasketModel
        fields = '__all__'


class BasketRetrieveSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True)

    class Meta:
        model = models.BasketModel
        fields = ('id', 'products')
