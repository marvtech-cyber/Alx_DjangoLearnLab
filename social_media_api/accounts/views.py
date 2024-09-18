
# Importing necessary modules
from rest_framework import generics, permissions, status  
from .serializers import UserSerializer  # Importing UserSerializer for serializing user data
from rest_framework.authtoken.views import ObtainAuthToken  # Importing ObtainAuthToken view for token-based authentication
from .models import CustomUser  # Importing CustomUser model for handling user-related operations
from django.shortcuts import get_object_or_404  # Importing get_object_or_404 for getting an object or raising a 404 error
from rest_framework.response import Response  # Importing Response class for custom responses
class RegisterView(generics.CreateAPIView):  # CreateAPIView for handling user registration
    serializer_class = UserSerializer  # Using UserSerializer for serializing user data
    permission_classes = [permissions.AllowAny]  # Allow any user to register

class LoginView(ObtainAuthToken):  # ObtainAuthToken view for handling user login
    def post(self, request, *args, **kwargs):  # Overriding post method to customize response
        serializer = self.serializer_class(data=request.data, context={'request': request})  # Creating a serializer instance with request data
        serializer.is_valid(raise_exception=True)  # Validating the serializer data
        user = serializer.validated_data['user']  # Getting the user object from serializer data
        user_serializer = UserSerializer(user)  # Creating a UserSerializer instance for the user object
        return Response(user_serializer.data)  # Returning a custom response with serialized user data

class ProfileView(generics.RetrieveUpdateAPIView):  # RetrieveUpdateAPIView for handling user profile retrieval and update
    serializer_class = UserSerializer  # Using UserSerializer for serializing user data
    permission_classes = [permissions.IsAuthenticated]  # Requiring authentication for accessing user profile

    def get_object(self):  # Overriding get_object method to return the current user object
        return self.request.user

