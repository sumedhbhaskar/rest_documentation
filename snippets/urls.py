from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns=[
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view() ),
    path('users/<int:pk>', views.UserDetail.as_view()),
    
]
