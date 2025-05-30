from typing import Type

from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from apps.products import models, serializers


@extend_schema(tags=['Товары'])
class ProductView(ReadOnlyModelViewSet):
    queryset = models.ProductModel.objects.all()

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == 'list':
            return serializers.ProductListSerializer
        return serializers.ProductRetrieveSerializer


@extend_schema(tags=['Меню'])
class MenuView(GenericViewSet, mixins.ListModelMixin):
    queryset = models.MenuModel.objects.all()
    serializer_class = serializers.MenuListSerializer


@extend_schema(tags=['Акции'])
class PromoView(ReadOnlyModelViewSet):
    queryset = models.PromoModel.objects.all()

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == 'list':
            return serializers.PromoListSerializer
        return serializers.PromoRetrieveSerializer


@extend_schema(tags=['Корзины'])
class BasketView(GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = models.BasketModel.objects.all()

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == 'retrieve':
            return serializers.BasketRetrieveSerializer
        return serializers.BasketBaseSerializer
