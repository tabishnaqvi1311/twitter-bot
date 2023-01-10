# The get_tweets function uses the user_timeline method of the Tweepy API to get the 10 most recent tweets from the specified user. The post_tweets function then iterates through these tweets and uses the update_status method to post them to the authenticated account's timeline.

# schedule_tweets uses the schedule library to schedule the post_tweets function to run every 2 minutes. The script also has a infinite loop that calls schedule's run_pending method which runs any scheduled tasks that are due to be run and then sleeps for 1 sec.

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
from tweepy import API
from tweepy import Cursor
from tweepy.errors import TweepyException
from tweepy import OAuthHandler

# Authenticate to Twitter
auth = tweepy.OAuthHandler("iB9LQqxubKW7wvLKAyltZgaOZ", "PORmKfASEYF9buYginDQzNxw0h9mf6L5QiuzrZW2Ncfsa9k7gW")
auth.set_access_token("1568647627075629056-YGXlgpvaTO4EC1lMkhJ0IxKC49wYgE", "hGReqICstQv0Fvvb9aKyww6BO7mLNroxbyF8HXWBuRdYU")
api = tweepy.API(auth)

def refresh_access_token():
    if api.access_token_expired:
        api.refresh_access_token()

def get_tweets():
    # Get tweets from specified user
    tweets = api.user_timeline(screen_name = "hourlyshitpost2", count = 24)
    return tweets

def post_tweets():
    tweets = get_tweets()
    for tweet in tweets:
        try:
            if 'media' in tweet.entities:
                media_list = tweet.entities['media']
                for media in media_list:
                    print(media['media_url'])
                    #posts meme using media_url
                    api.update_status(status=tweet.text, media_ids=[media['media_id']])
            else:
                api.update_status(tweet.text)
            print("Tweet posted: " + tweet.text)
        except tweepy.TweepyException as error:
            print(error.reason)
            continue

def schedule_tweets():
    # Schedule tweets to be posted every hour
    schedule.every().hour.do(post_tweets)
    schedule.every().hour.do(refresh_access_token)

if __name__ == "__main__":
    schedule_tweets()
    while True:
        schedule.run_pending()
        time.sleep(1)

# print(api)
# startTime = time.time()
# tweets = api.search_tweets( q = 'funny' )
# for tweet in range(tweets):
#     try:
#         api.update_status(tweet.text)
#         print("Tweet #{} posted!".format(tweet+1))
#     except tweepy.error.TweepError as e:
#         print("Error: {}",format(e))
#     time.sleep(60)

# elapsedTime = time.time() - startTime

# print("All tweets have been posted in {} seconds".format(elapsedTime))