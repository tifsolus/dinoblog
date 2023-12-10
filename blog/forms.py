''' 
@Program: forms
@Author: Donald Osgood
@Last Date: 2023-12-09 18:27:05
@Purpose:Donald Osgood
'''
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)