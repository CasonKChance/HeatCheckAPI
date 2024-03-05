from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('emailAddress', 'firstName', 'lastName', 'password', 'position',
                  'hometown', 'skillLevel', 'height', 'weight', 'ageGroup', 'playType')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
