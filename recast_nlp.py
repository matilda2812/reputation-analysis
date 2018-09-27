# make calls to recast natural language processing API
# why reinvent the wheel?

import requests
import recastai
import json
from twitter_scraper import scrape
from collections import defaultdict

DEV_TOKEN = "f9f4b8e63de484bac22545c58166442b"

# URL to make recast requests to
BASE_URL = "https://api.recast.ai/v2/request"
BLUESCOPE= "search?q=bluescope&src=typd"
SAP="search?q=%40sap&src=typd"
ZUCKERBERG='search?q=Mark%20Zuckerberg&src=tyah'
SAP_ANZ='search?q=sap%20anz&src=typd'
MARCUS='marcustlim?lang=en'
MICROSOFT='search?q=microsoft&src=typd'
VILLAGE_ROADSHOW='search?q=village%20roadshow&src=typd'


# Endpoint for API (fi required)


# function to analyse given text
def analyse_text(text):

    make_request("")

def sentiment_analysis(query):
    tweets = scrape(query)

    # dictionary to store count of tweet sentiments
    sentiment_dict = defaultdict(int)

    for tweet in tweets:
        sentiment = make_request(tweet)
        sentiment_dict[sentiment] += 1
    print(sentiment_dict)


def analyse_sentiment():
    return



def make_request(text):
    url = BASE_URL

    language = "en"

    request = recastai.Request(DEV_TOKEN, language)
    response = request.analyse_text(text)
    sentiment = json.loads(response.raw)['results']['sentiment']
    return sentiment

sentiment_analysis(VILLAGE_ROADSHOW)
