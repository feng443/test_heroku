# Dependencies
import numpy as np
import pandas as pd
import tweepy
import time
import json
import time
# Twitter API Keys

import os
import sys
sys.path.append(os.path.join(
    r'C:\Users\feng443\OneDrive',
    r'Data Science Bootcamp\git\RUDSClassRoomExcercise',
    r'Python\API\Twitter API'))

from config import *
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_TOKEN_SECRET)

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target Term
my_username = "@feng443"
conversation_partner = "@feng443"

# Send opening message to conversation partner
print('init')
api.update_status("Hey %s! How's it going?" % conversation_partner)

# Response Lines
# @TODO: Create a list of Response Lines
lines = ['hi2', 'hello2', 'aloha2']

# # @TODO: Create converse function
#
def converse(partner):
    now = time.time()
    api.update_status(f"@partner {now} ")

def respond(partner):
#     # @TODO: Find the latest tweet from conversation_partner
    now = time.time()
    for tweet in api.search(partner, count=1, result_type='recent')['statuses']:
        tweet_id = tweet['id']
        tweet_text = tweet['text']
        print(tweet_id)
        print(tweet_text)
        text = lines.pop()
        print('reply' + text)
        #api.update_status(msg)
        api.update_status(f'@{partner}: {text}', in_reply_to_status_id=tweet_id)
#         # @TODO: Respond to the tweet with one of the response lines
#
while lines:
    respond(conversation_partner)
    time.sleep(10)
    print('while')
# @TODO: Set timer to run every minute

