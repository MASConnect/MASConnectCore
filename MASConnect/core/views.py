from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from django.http import Http404

# Create your views here.

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        pk = self.kwargs.pop('pk', None)
        if not pk:
            raise Http404
        if pk == 'me':
            self.kwargs['pk'] = self.request.user.pk
        return super(UserViewSet, self).get_object()

class ChapterViewSet(ModelViewSet):
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()
