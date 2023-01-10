import time
import schedule
import tweepy
import twitter
from tweepy import API
from tweepy import Cursor
from tweepy.errors import TweepyException
from tweepy import OAuthHandler
import random

# Authenticate to Twitter
auth = tweepy.OAuthHandler("API KEY", "API KEY SECRET")
auth.set_access_token("ACCESS TOKEN", "ACCESS TOKEN KEY")
api = tweepy.API(auth)

def refresh_access_token():
    if api.access_token_expired:
        api.refresh_access_token()

def time_left():
    print("Time : ", time.ctime())

def get_tweets(username):
    print("Fetching Tweet...")
    # Get tweets from specified user
    tweets = api.user_timeline(screen_name = username, count = 200)
    return tweets

def post_tweet(tweet):
    try:
        tweets = api.user_timeline()
        for t in tweets:
            if t.text == tweet.text:
                print("Skipping duplicate tweet: " + tweet.text)
                return
        print("Posting Tweet...")
        api.update_status(tweet.text)
        print("Tweet posted: " + tweet.text)
    except tweepy.TweepyException as error:
        print(error.reason)

def schedule_tweets():
    tweets = get_tweets("insert user name here}")
    tweet = random.choice(tweets)
    post_tweet(tweet)
    # Schedule tweets to be posted every hour
    schedule.every(1).minutes.do(time_left)
    schedule.every(2).minutes.do(schedule_tweets)
    schedule.every(60).minutes.do(refresh_access_token)

if __name__ == "__main__":
    print("Initiating..")
    schedule_tweets()
    while True:
        schedule.run_pending()
        time.sleep(1)