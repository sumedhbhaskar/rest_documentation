from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions


class SnippetList(generics.ListCreateAPIView):
    """
    list all the snippets and create new snippet

    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes= (permissions.IsAuthenticatedOrReadOnly,)  

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Now this contain detailed view of a snippet, it can be updated, deleted or retrived
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes= (permissions.IsAuthenticatedOrReadOnly,)  


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer        
