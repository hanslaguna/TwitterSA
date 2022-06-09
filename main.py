import pandas as pd
import tweepy
import config

# Keys
api_key = config.API_KEY
api_key_secret = config.API_SECRET
bearer_token = config.BEARER_TOKEN
access_token = config.ACCESS_TOKEN
access_token_secret = config.ACCESS_TOKEN_SECRET

# Authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Query Segment
query = '#JusticeForJohnnyDepp || #JusticeForAmberHeard -filter:retweets'
language = 'en'

results = api.search_tweets(tweet_mode='extended', count='100', q=query, lang=language)

# Compile into csv dataset
columns = ['Time', 'User', 'Tweet']
data = []

for tweet in results:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv', encoding='utf-8-sig')
