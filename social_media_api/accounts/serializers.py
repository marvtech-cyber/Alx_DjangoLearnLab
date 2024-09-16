from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)