from django.urls import path
from . import views

urlpatterns = [
    #Empty path for the default home page
    path('', views.homePage, name='blog-home'),
    path('about/', views.aboutPage, name='blog-about'),
]
