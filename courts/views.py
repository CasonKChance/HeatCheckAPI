from rest_framework import generics
from .models import Court
from .serializers import CourtSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny


class CourtListCreate(generics.ListCreateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer


class CourtRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

class CourtListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        courts = Court.objects.all()

        serializer = CourtSerializer(courts, many=True)
        return Response(serializer.data)
    
class CourtSpecificView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        court_id = request.data.get('id')
        court = Court.objects.filter(id=court_id)

        serializer = CourtSerializer(court)
        return Response(serializer.data)