from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)


urlpatterns = [
    #Empty path for the default home page
    path('', PostListView.as_view(), name='blog-home'),
    #To view each posts individually
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #For updating a post in the frontend of the site:
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    #For deleting a post:
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    #For creating a new post:
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    #About path for the about page
    path('about/', views.aboutPage, name='blog-about'),
    
]
