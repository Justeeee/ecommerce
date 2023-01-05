from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError

from apps.user.models import User


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
        fields = ('id', 'username','email', 'password', 'confirm_password',)


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class GetMeModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone')
