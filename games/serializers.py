from rest_framework import serializers
from .models import Game
from users.serializers import UserSerializer


class GameSerializer(serializers.ModelSerializer):
    players_associated = UserSerializer(many=True, read_only=True)
    court_details = serializers.ReadOnlyField(source='court.address')

    class Meta:
        model = Game
        fields = ('gameID', 'court', 'court_details', 'players_associated')


class GameCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('gameID', 'court', 'players_associated')

    def create(self, validated_data):
        players = validated_data.pop('players_associated')
        game = Game.objects.create(**validated_data)
        game.players_associated.set(players)
        return game

    def update(self, instance, validated_data):
        instance.court = validated_data.get('court', instance.court)
        if 'players_associated' in validated_data:
            players = validated_data.pop('players_associated')
            instance.players_associated.set(players)
        instance.save()
        return instance
