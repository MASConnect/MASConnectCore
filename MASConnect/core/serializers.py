from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user