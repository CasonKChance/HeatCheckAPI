from rest_framework import generics
from .models import Court
from .serializers import CourtSerializer


class CourtListCreate(generics.ListCreateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer


class CourtRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer
