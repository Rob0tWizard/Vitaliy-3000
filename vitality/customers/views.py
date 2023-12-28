from django.contrib.auth import login, authenticate
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from .serializers import UserSerializer


class RegisterApiView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        return Response({'refresh': str(refresh), 'access': str(access_token)}, status=status.HTTP_201_CREATED)


class LoginApiView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Invalid request. Both username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            return Response({'refresh': str(refresh), 'access': str(access_token)}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid.'}, status=status.HTTP_401_UNAUTHORIZED)


