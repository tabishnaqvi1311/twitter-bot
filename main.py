import time
import schedule
import tweepy
import twitter
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
import random

# Authenticate to Twitter
auth = tweepy.OAuthHandler("API KEY", "API KEY SECRET")
auth.set_access_token("ACCESS TOKEN", "ACCESS TOKEN KEY")
api = tweepy.API(auth)

def get_tweets(username):
    print("Fetching Tweet...")
    # Get n tweets from specified user
    tweets = api.user_timeline(screen_name=username, count=500)
    return tweets

def post_tweet(tweet):
    tweets = api.user_timeline()
    for t in tweets:
            if t.text == tweet.text:
            # Skipping any duplicate tweet
                print("Skipped duplicate tweet: " + tweet.text)
                schedule_tweets()
                continue
    print("Posting Tweet...")
    api.update_status(tweet.text)  # posting the tweet
    print("Successfully Posted : " + tweet.text + " at : " + time.ctime())
    print("\n")

def schedule_tweets():
    tweets = get_tweets("hi1ar10us")
    tweet = random.choice(tweets)
    print("Fetched Tweet : " + tweet.text)
    post_tweet(tweet)

if __name__ == "__main__":
    print("Getting Ready...\n")
    schedule.every(60).minutes.do(schedule_tweets)
    while True:
        schedule.run_pending()
        time.sleep(1)
