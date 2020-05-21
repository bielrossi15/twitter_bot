# tweepy-bots/bots/config.py
import tweepy
import logging
import os

log = logging.getLogger()

def create_api():
    consumer_key = "eWtnnavN6wwqgNwuY1Vg4BW7s"
    consumer_secret = "sLQ0gG0rghFVz85BTFHYYsKonFzRyZHS2vh4dcbaJMBl3XiXfd"
    access_token = "1263452933133402114-olHNctnboo9EgoJVaDrm9FQ6h8V30I"
    access_token_secret = "UwCUJMEiugHS5hBbeWdkRRAV9bQAM3UWhlGUR4sBWfzfB"
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
