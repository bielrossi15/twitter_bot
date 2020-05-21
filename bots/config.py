# tweepy-bots/bots/config.py
import tweepy
import logging
import os

log = logging.getLogger()

def create_api():
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
    except Exception as e:
        log.error("error creating api", exc_info=True)
        raise e
    
    log.info("api created")
    return api
