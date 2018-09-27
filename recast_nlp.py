# make calls to recast natural language processing API
# why reinvent the wheel?

import requests
import recastai
import json
from twitter_scraper import scrape
from collections import defaultdict
import re

DEV_TOKEN = "f9f4b8e63de484bac22545c58166442b"

# URL to make recast requests to
BASE_URL = "https://api.recast.ai/v2/request"



# Endpoint for API (fi required)


# function to analyse given text
def analyse_text(text):

    make_request("")

def sentiment_analysis(query):
    with open('searches.json') as f:
        queries = json.load(f)

    tweets = scrape(queries[query])

    # dictionary to store count of tweet sentiments
    sentiment_dict = defaultdict(int)

    for tweet in tweets:
        sanitised_tweet = re.sub(r"http\S+", "", tweet)
        sentiment = make_request(sanitised_tweet)
        sentiment_dict[sentiment] += 1
        print(sanitised_tweet)
    print(sentiment_dict)


def analyse_sentiment(sentiment):
    total = sum(d.values())
    return



def make_request(text):
    url = BASE_URL

    language = "en"

    request = recastai.Request(DEV_TOKEN, language)
    response = request.analyse_text(text)
    sentiment = json.loads(response.raw)['results']['sentiment']
    return sentiment

sentiment_analysis("marcus")
