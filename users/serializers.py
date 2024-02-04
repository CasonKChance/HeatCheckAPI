from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'emailAddress', 'position',
                  'hometown', 'skillLevel', 'height', 'weight', 'ageGroup', 'playType', "playerID")
