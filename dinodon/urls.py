''' 
@Program: urls
@Author: Donald Osgood
@Last Date: 2023-11-18 21:41:14
@Purpose:Donald Osgood
'''
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
     path('accounts/login/', views.LoginView.as_view(), name='login'),
     path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]