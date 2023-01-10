## THIS IS AN ONGOING PROJECT. ANY AND ALL CONTRIBUTIONS, ISSUES ARE APPRECIATED.

#### The get_tweets function uses the user_timeline method of the Tweepy API to get the 10   most recent tweets from the specified user. The post_tweets function then iterates through these tweets and uses the update_status method to post them to the authenticated account's timeline.

#### schedule_tweets uses the schedule library to schedule the post_tweets function to run every 2 minutes. The script also has a infinite loop that calls schedule's run_pending method which runs any scheduled tasks that are due to be run and then sleeps for 1 sec.

