#!/usr/bin/env python
'''
sentiments.py
App implements a sentiment analysis function. 
'''
import re
import json
import warnings
import traceback
from textblob import TextBlob
warnings.filterwarnings("ignore")

def extract_and_clean_text(raw_tweet):
    tweet = raw_tweet['text']
    '''
     Utility function to clean tweet text by removing links, special characters
     using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(tweet)
    return analysis.sentiment.polarity

def build_result(polarity, tweet):
    result = {}
    try:
        result['polarity']=round(polarity,2)
        result['text']= tweet
        return json.dumps(result)
    except Exception:
        traceback.print_exc()
        return json.dumps(result)

def process(data):
    raw_tweet = json.loads(data)
    tweet = extract_and_clean_text(raw_tweet)
    return build_result(get_tweet_sentiment(tweet),tweet)

if __name__ == "__main__":
    while True:
        try:
            data = input()
            print(process(data))
        except EOFError:
            exit(0)
       

