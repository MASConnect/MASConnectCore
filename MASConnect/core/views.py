from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *

# Create your views here.

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ChapterViewSet(ModelViewSet):
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()
