from django.utils import translation
import jsend

from rest_framework import serializers, exceptions
from rest_auth.serializers import LoginSerializer
from rest_auth.registration.serializers import RegisterSerializer

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


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "phone_number", "date_of_birth"]


class LoginSerializer(LoginSerializer):
    username = None

    class Meta:
        model = CustomUser
        fields = ["id", "email", "password"]


class RegisterSerializer(RegisterSerializer):
    username = None
    password1 = serializers.CharField(write_only=True, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})
    phone_number = serializers.CharField(max_length=11)
    date_of_birth = serializers.CharField(max_length=8)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "password1",
            "password2",
            "phone_number",
            "date_of_birth",
        ]

    def save(self, request):
        user = super().save(request)
        user.phone_number = self.data.get("phone_number")
        user.date_of_birth = self.data.get("date_of_birth")
        user.save()
        return user
