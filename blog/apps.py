''' 
@Program: apps
@Author: Donald Osgood
@Last Date: 2023-11-30 20:53:53
@Purpose: Blog Configuration File
'''
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """The blog config

    Args:
        AppConfig (AppConfig): Application Configuration Object
    """    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
