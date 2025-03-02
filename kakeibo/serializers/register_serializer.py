from rest_framework import serializers
from kakeibo.models import CustomUser


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100, min_length=6)
    birthday = serializers.DateField()

    def validate_email(self, value):
        is_exists = CustomUser.objects.filter(email__iexact=value).exists()
        if is_exists:
            raise serializers.ValidationError("Email already registered")
        return value

    def validate_username(self, value):
        is_exists = CustomUser.objects.filter(email__iexact=value).exists()
        if is_exists:
            raise serializers.ValidationError("Username already exists")
        return value
