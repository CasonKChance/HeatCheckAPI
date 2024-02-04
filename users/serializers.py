from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('playerID', 'firstName', 'lastName', 'emailAddress',
                  'height', 'weight', 'age', 'skill_level', 'position')
