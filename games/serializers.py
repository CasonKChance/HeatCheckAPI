from rest_framework import serializers
from .models import Game
from users.serializers import UserSerializer


class GameSerializer(serializers.ModelSerializer):
    players_associated = UserSerializer(many=True, read_only=True)
    court_details = serializers.ReadOnlyField(source='court.address')

    class Meta:
        model = Game
        fields = ('gameID', 'court', 'court_details', 'players_associated')
