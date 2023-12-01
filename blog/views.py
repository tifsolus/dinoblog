""" 
@Program: views
@Author: Donald Osgood
@Last Date: 2023-11-18 21:48:29
@Purpose: The default blog view
"""
from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    """_summary_

    Args:
        request (flask): flask request object

    Returns:
        html: html to rend to the screen
    """    
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blog/post_list.html", {'posts': posts})
