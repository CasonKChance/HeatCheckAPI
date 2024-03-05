from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # If you have a detail view, you might want to return the URL to the created resource
            return Response({'id': user.pk}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            return Response({'message': 'Login Successful', 'id': user.pk}, status=status.HTTP_201_CREATED)
        
        return Response({'message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class UserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class UserSearch(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = CustomUser.objects.all()
        first_name = self.request.query_params.get('firstName')
        last_name = self.request.query_params.get('lastName')
        if first_name:
            queryset = queryset.filter(firstName__icontains=first_name)
        if last_name:
            queryset = queryset.filter(lastName__icontains=last_name)
        return queryset
