from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User



"""
this model serializer is just a shortcut for creating serializer classes

it is a default implimentation of create() and update() methods

In hyperlinked serializers we need to name our urlpatterns because hyperlink refers to those by name

"""

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url' , 'highlight' ,'owner', 'id', 'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.HyperlinkedModelSerializer):
#    snippets = serializers.HyperlinkedRelatedField( many=True, view_name='snippet-detail', read_only=True )

    class Meta:
        model = User
        fields = ( 'url' ,'id', 'username', 'snippets')        