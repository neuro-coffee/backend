from rest_framework import serializers
from rest_framework.validators import ValidationError

from apps.users import models


class RetrieveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        exclude = ('password',)


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = models.UserModel
        fields = ['id', 'username', 'password', 'password_confirmation', 'email']

    def create(self, validated_data: dict) -> models.UserModel:
        user = models.UserModel.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
        )
        return user

    def validate(self, attrs: dict) -> dict:
        if attrs['password'] != attrs.pop('password_confirmation'):
            raise ValidationError('Введенные пароли не совпадают')
        return attrs
