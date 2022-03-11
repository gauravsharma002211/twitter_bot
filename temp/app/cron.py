import tweepy
from .models import *
import json
import requests

def my_scheduled_job():
    # authentication keys
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAPJJaAEAAAAAMAcBxUHFJOOmma1McKEX5VrXXYg%3D5baIUqkFLYpBJs99IXux6eWEFSuNPIue0UwQBswyBwbrYIiaAG"

    # fetching user handles to find follower count for
    user_data = UserRequired.objects.all()

    user_list = ""

    # empty list failsafe
    for i in user_data:
        if user_list == "":
            user_list = i.list_of_users 
        else:
            user_list = user_list+","+i.list_of_users

    header = {
        "Authorization" : f"Bearer {bearer_token}"
    }

    #Api call for inserted user handle - response includes user data with follow count
    resp = requests.get(f"https://api.twitter.com/2/users/by?usernames={user_list}&user.fields=public_metrics", headers = header)

    print(resp.text)

    #fetch follow count and user handle
    for i in json.loads(resp.text)['data']:
        count = i['public_metrics']['followers_count']
        uname = i['username']

        # If user handle already exist then just update
        obj = FollowerCount.objects.filter(name = uname)

        if obj:
            f_obj = obj.first()
            f_obj.count = count
            f_obj.save()
        
        # save follow count for user handle into database
        else:
            x=FollowerCount(name=uname,count=count)
            x.save()