""" 
@Program: models
@Author: Donald Osgood
@Last Date: 2023-11-18 19:12:59
@Purpose: Store Models as part MVC
"""
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    """Post Model for blog posts

    Args:
        models (model class): Model Class

    Returns:
        Post: returns post model
    """    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
