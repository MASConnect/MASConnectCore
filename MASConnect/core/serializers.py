from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def validate_password(self, value):
        return make_password(value)

class ChapterSerializer(ModelSerializer):

    class Meta:
        model = Chapter
        fields = "__all__"

