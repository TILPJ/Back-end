import jsend

from rest_framework import serializers, exceptions
from rest_auth.serializers import LoginSerializer

from .models import CustomUser


class UserCheckSerializer(serializers.ModelSerializer):
    email_check = serializers.SerializerMethodField()

    def get_email_check(self, instance):
        if instance:
            return True
        else:
            return False

    class Meta:
        model = CustomUser
        fields = ["email_check"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "phone_number", "date_of_birth"]


class LoginSerializer(LoginSerializer):
    username = None

    class Meta:
        model = CustomUser
        fields = ["id", "email", "password"]
