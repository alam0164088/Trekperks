from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Password লুকানো থাকবে

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  # Password হ্যাশ করে সেভ করবে
        user.save()
        return user
