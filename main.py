# In this script, we first import the tweepy library, which is used to interact with the Twitter API, and the time library, which is used to schedule the tweets. Next, we authenticate with the Twitter API using our API key, API secret, access token, and access token secret. Then, we define the number of tweets to be posted and the interval between them (in seconds).

# Then, we get the current time and enter a loop that will run for the number of tweets we want to post. Within the loop, we use the api.update_status() method to post a tweet. We have used "This is tweet #{}".format(i+1) as a text for tweet, you can change it with whatever you want. In addition, you can also add an image or video using the api.update_with_media() method.

# After each tweet, the script will sleep for interval seconds. Once all tweets have been posted, the script will calculate the elapsed time and print a message indicating that all tweets have been posted.


import base64
import hashlib
import os
import re
import json
import requests
import redis
from requests.auth import AuthBase, HTTPBasicAuth
from requests_oauthlib import OAuth2Session, TokenUpdated
from flask import Flask, request, redirect, session, url_for, render_template
import time
import schedule
import tweepy
import twitter

auth = tweepy.OAuthHandler("iB9LQqxubKW7wvLKAyltZgaOZ", "PORmKfASEYF9buYginDQzNxw0h9mf6L5QiuzrZW2Ncfsa9k7gW")
auth.set_access_token("1568647627075629056-YGXlgpvaTO4EC1lMkhJ0IxKC49wYgE", "hGReqICstQv0Fvvb9aKyww6BO7mLNroxbyF8HXWBuRdYU")
api = tweepy.API("AAAAAAAAAAAAAAAAAAAAAJ%2BJlAEAAAAAU0leZ2ViAf03%2BmwuimxaNnkuhiQ%3D7oHCRnQz0F14UgYdMfU2nrndbrY2Ztj45esdxIv3tKeGXqFz7M")

# print(api)
startTime = time.time()
tweets = api.search_tweets( q = 'funny' )
for tweet in range(tweets):
    try:
        api.update_status(tweet.text)
        print("Tweet #{} posted!".format(tweet+1))
    except tweepy.error.TweepError as e:
        print("Error: {}",format(e))
    time.sleep(60)

elapsedTime = time.time() - startTime

print("All tweets have been posted in {} seconds".format(elapsedTime))

# In this script, we first import the tweepy library, which is used to interact with the Twitter API, and the time library, which is used to schedule the tweets. Next, we authenticate with the Twitter API using our API key, API secret, access token, and access token secret. Then, we define the number of tweets to be posted and the interval between them (in seconds).

# Then, we get the current time and enter a loop that will run for the number of tweets we want to post. Within the loop, we use the api.update_status() method to post a tweet. We have used "This is tweet #{}".format(i+1) as a text for tweet, you can change it with whatever you want. In addition, you can also add an image or video using the api.update_with_media() method.

# After each tweet, the script will sleep for interval seconds. Once all tweets have been posted, the script will calculate the elapsed time and print a message indicating that all tweets have been posted.

