import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")
api = tweepy.API(auth)

# Confirm authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print("Error during authentication")
    raise e

# Delete all tweets
for tweet in tweepy.Cursor(api.user_timeline).items():
    api.destroy_status(tweet.id)
    print("Deleted tweet:", tweet.id)
