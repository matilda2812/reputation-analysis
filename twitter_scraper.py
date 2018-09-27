import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# Twitter search url
BASE_URL = u'https://twitter.com/'
BASE_LEGACY_URL = u'https://mobile.twitter.com/'

SAP_SEARCH = u'search?q=%40sap&src=typd'
SAP_LEGACY_SEARCH = u'search?q=sap&s=typd&x=0&y=0'


# use selenium to start a web browser
def open_browser(query):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get(BASE_URL+query)
    return driver.page_source


def scrape(query):
    webpage = open_browser(query)

    # initialise html parser
    # print(r.text)
    soup = BeautifulSoup(webpage, 'html.parser')
    tweets = [p.text for p in soup.find_all('p',class_='tweet-text')]
    return tweets


# scrape(SAP_SEARCH)
