from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):

    class Meta:
        model = User

    def validate_password(self, value):
        return make_password(value)