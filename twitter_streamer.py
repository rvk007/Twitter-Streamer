import keys

import os
import tweepy as tp
import pandas as pd

consumer_authentication = tp.OAuthHandler(keys.consumer_key,keys.consumer_key_secret)
consumer_authentication.set_access_token(keys.access_token,keys.access_token_secret)
api = tp.API(consumer_authentication,wait_on_rate_limit =True)

print("Twitter API connected")

search = "Tesla"
date = "2019-08-19"

tweets = tp.Cursor(api.search,q=search,lang="en",since=date).items(5)

tweet_result = [[x.text,x.user.location,x.user.screen_name] for x in tweets]
tweet_username = [x.user.screen_name for x in tweets]
print(tweet_result[2])
print("GAP")
print(tweet_result)
print("GAP@")
print(tweet_username)
print()




""" TODO
use filter-retweet in tweet_result
practice various method
"""