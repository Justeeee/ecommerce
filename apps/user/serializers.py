from apps.user.models import User
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError


class UserCreateModelSerializer(ModelSerializer):
    password = CharField(max_length=255, write_only=True)
    confirm_password = CharField(max_length=255, write_only=True)

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        password = attrs.get('password')
        if confirm_password != password:
            raise ValidationError("Password didn't match")
        attrs['password'] = make_password(password)
        validated_data = super().validate(attrs)

        return validated_data

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'confirm_password',)


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password',)


class LogOutSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)


class ClientModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class MerchantModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'date_joined')


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)
