import tweepy
import logging
from config import create_api


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FavRtListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        try:
            tweet.favorite()
        except Exception as e:
            logger.error("Error on fav", exc_info=True)
            
        if not tweet.retweeted:
            try:
                tweet.retweet()
                print("fav and rt @" + tweet.user.screen_name)
            except Exception as e:
                logger.error("Error on rt", exc_info=True)
        

    def on_error(self, status):
        logger.error(status)

    
def main():
    api = create_api()
    listener = FavRtListener(api)
    stream = tweepy.Stream(api.auth, listener)
    stream.filter(track=["to puto", "to puta"])

if __name__ == "__main__":
    main()

