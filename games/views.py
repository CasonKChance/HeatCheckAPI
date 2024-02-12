from rest_framework import generics
from .models import Game
from .serializers import GameSerializer, GameCreateUpdateSerializer


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
