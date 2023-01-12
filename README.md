# Twitter Bot 

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This script is a Python bot that posts tweets from a given user's timeline every hour.

## Getting Started <a name = "getting_started"></a>

Add your Twitter API credentials in the specified place in the script.

You can change the target user by replacing 'username' with the desired username
Run the script.

### Prerequisites

In order to run the above script, you will need to have Python and the following libraries installed:

   - tweepy
   - schedule
   - twitter

You also need to have a developer account of twitter and setup access keys and tokens.

### Installing

You can install them using pip by running the command pip install tweepy schedule twitter on the command line.
You also need to have a developer account of twitter and setup access keys and tokens.

    pip install tweepy
    pip install twitter
    pip install schedule

The code uses your twitter developer account's access keys and tokens to authenticate and interact with the twitter API. The script uses the tweepy library to interact with the Twitter API.

## Usage <a name = "usage"></a>

Make sure to keep the script running in order for the tweets to be posted at regular intervals.
You can use a cloud/hosting service, I used PythonAnywhere

The script will now post a random tweet from the given user's timeline every hour, and also logs the time at which the tweet was posted.

You can change the scheduling time by modifying the value of the "schedule.every(60).minutes.do(schedule_tweets)" line in the script.

Also, you can use this script locally on your computer.
