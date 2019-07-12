from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

"""
urlpatterns=[
    path('', views.api_root),
    
    path('snippets/', 
    views.SnippetList.as_view(),
    name='snippet-list' ),

    path('snippets/<int:pk>', 
    views.SnippetDetail.as_view(), 
    name='snippet-detail'),
    
    path('users/', 
    views.UserList.as_view(), 
    name='user-list' ),
    
    path('users/<int:pk>', 
    views.UserDetail.as_view(), 
    name='user-detail'),
    
    path('snippets/<int:pk>/highlight/', 
    views.SnippetHighlight.as_view(), 
    name='snippet-highlight')
    
]
"""

router= DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

urlpatterns=[
    path('', include(router.urls)),

    
    path('snippets/<int:pk>/highlight/', 
    snippet_highlight, 
    name='snippet-highlight')
]

