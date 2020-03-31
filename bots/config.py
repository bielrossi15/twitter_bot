# tweepy-bots/bots/config.py
import tweepy
import logging
import os

log = logging.getLogger()

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    auth = tweepy.OAuthHandler("fayA9tzVCd8w2mEsjDegB685U", "OchZUygZm14Du8jgziHCAFs7ZH1NQZI2PZgITkHhwWsPOI8KS4")
    auth.set_access_token("1244755774854893569-tNk42eHSqWO2Kwt9kgCOmKvFKU6bWZ", "f2vr1PXDtVdpxQQSU4UK6I6tHCGNMQ1SAJmqfdkJ2NPJu")

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        log.error("error creating api", exc_info=True)
        raise e
    
    log.info("api created")
    return api
