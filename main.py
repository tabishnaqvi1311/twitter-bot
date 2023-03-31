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

def get_tweets():
    print("Fetching Tweet...")
    with open("tweets.txt", "r") as f:
        tweets = f.readlines()
    # print("Fetching Tweet...")
    # Get n tweets from specified user
    # tweets = api.user_timeline(screen_name=username, count=500)
    return tweets

def post_tweet(tweet):
    tweets = api.user_timeline()
    for t in tweets:
            if t.text == tweet:
            # Skipping any duplicate tweet
                print("Skipped duplicate tweet: " + tweet)
                schedule_tweets()
                continue
    print("Posting Tweet...")
    api.update_status(tweet)  # posting the tweet
    print("Successfully Posted : " + tweet + " at : " + time.ctime())
    print("\n")

def schedule_tweets():
    tweets = get_tweets()
    tweet = random.choice(tweets)
    tweet = tweet.strip()
    print("Fetched Tweet : " + tweet)
    post_tweet(tweet)

if __name__ == "__main__":
    print("Getting Ready...\n")
    schedule.every(24).hours.do(schedule_tweets)
    while True:
        schedule.run_pending()
        time.sleep(1)
