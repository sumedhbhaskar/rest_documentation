from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    list all the snippets and create new snippet

    """
    querysets = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Now this contain detailed view of a snippet, it can be updated, deleted or retrived
    """
    querysets = Snippet.objects.all()
    serializer_class = SnippetSerializer
