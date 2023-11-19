''' 
@Program: urls
@Author: Donald Osgood
@Last Date: 2023-11-18 21:42:12
@Purpose:Donald Osgood
'''
from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
]