'''
urls.py is created in the my_web_demo directory
'''

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home, name='home'),
]
