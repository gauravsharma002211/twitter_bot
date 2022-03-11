from textwrap import indent
from django.urls import path,include
from . import views

urlpatterns = [
    path('get_data/', views.TwitterFollowers.as_view())
]