from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)
