from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets



#@api_view(['GET'])
#def api_root(request, format = None):
#    return Response({
#        'users':reverse('user-list', request=request, format=format),
#        'snippets':reverse('snippet-list', request=request, format=format)
#
#    })


# class SnippetHighlight(generics.GenericAPIView):
#    queryset = Snippet.objects.all()
#    renderer_classes = (renderers.StaticHTMLRenderer,)

#    def get(self, request, *args, **kwargs):
#        snippet = self.get_object()
#        return Response(snippet.highlighted)




#class SnippetList(generics.ListCreateAPIView):
#"""
#   list all the snippets and create new snippet

#"""
#    queryset = Snippet.objects.all()
#    serializer_class = SnippetSerializer

#    def perform_create(self, serializer):
#        serializer.save(owner=self.request.user)

#    permission_classes= (permissions.IsAuthenticatedOrReadOnly,)  

#class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

#    """
#    Now this contain detailed view of a snippet, it can be updated, deleted or retrived
#    """
#    queryset = Snippet.objects.all()
#    serializer_class = SnippetSerializer

#    permission_classes= (permissions.IsAuthenticatedOrReadOnly,)  


# class UserList(generics.ListAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer      

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class= SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @action(detail = True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *a, **b):
        return Response(self.get_object().highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)    

    



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
