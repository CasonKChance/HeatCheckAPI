from rest_framework import generics
from .models import Game
from .serializers import GameSerializer, GameCreateUpdateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Game
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return GameCreateUpdateSerializer
        return GameSerializer


class GameRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return GameCreateUpdateSerializer
        return GameSerializer


class JoinOrCreateGame(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        court_id = request.data.get('court_id')

        if not court_id:
            return Response({'error': 'Court ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if there's an existing game with spots available for the given court
        game = Game.objects.filter(
            court_id=court_id, players__lt=F('players_needed')).first()

        if game:
            # Check if user is already part of the game
            if game.players.filter(id=user.id).exists():
                return Response({'message': 'User already part of the game.'}, status=status.HTTP_400_BAD_REQUEST)

            # Add user to the game
            game.players.add(user)
            message = 'User added to existing game.'
        else:
            # Create a new game and add the user
            game = Game.objects.create(court_id=court_id)
            game.players.add(user)
            message = 'New game created and user added.'

        # You might want to return the game details in the response
        return Response({'message': message, 'game_id': game.id}, status=status.HTTP_201_CREATED)


def court_players_count(request, court_id):
    court = get_object_or_404(Court, pk=court_id)
    game = court.games.first()  # Assuming only one game per court at a time

    if game:
        players_count = game.players_associated.count()
        return JsonResponse({
            'court_id': court_id,
            'players_count': players_count,
            'status': 'success'
        })
    else:
        return JsonResponse({
            'court_id': court_id,
            'message': 'No game currently associated with this court.',
            'status': 'error'
        })
