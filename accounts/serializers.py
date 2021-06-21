from rest_framework import serializers

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
