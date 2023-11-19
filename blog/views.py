''' 
@Program: views
@Author: Donald Osgood
@Last Date: 2023-11-18 21:48:29
@Purpose:Donald Osgood
'''
from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})