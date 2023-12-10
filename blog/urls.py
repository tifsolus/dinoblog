""" 
@Program: urls
@Author: Donald Osgood
@Last Date: 2023-11-18 21:42:12
@Purpose: Set post url path as default
"""
from django.urls import path
from . import views


urlpatterns = [
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
   path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
      path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
       path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
