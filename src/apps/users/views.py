from typing import Type

from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet

from apps.users import models, serializers


@extend_schema(tags=['Пользователи'])
class UserView(GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = models.UserModel.objects.all()

    def get_permissions(self) -> list[BasePermission]:
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == 'create':
            return serializers.RegisterUserSerializer
        return serializers.RetrieveUserSerializer
