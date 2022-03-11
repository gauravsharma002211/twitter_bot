from urllib import request
from django.shortcuts import render
import tweepy
from .models import FollowerCount

from rest_framework.views import APIView
from django.core import serializers
from django.http import HttpResponse
import json

# returns the user name with follows
class TwitterFollowers(APIView):

    def get(self,request):
        qs = FollowerCount.objects.all()

        post_list = []

        for data in qs:
            post_list.append({"username":data.name,"count":data.count})

        return HttpResponse(json.dumps(post_list))



