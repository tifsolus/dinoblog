""" 
@Program: urls
@Author: Donald Osgood
@Last Date: 2023-11-18 21:42:12
@Purpose: Set post url path as default
"""
from django.urls import path
from . import views

urlpatterns = [
      path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
       path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
