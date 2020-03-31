import tweepy
import logging
from config import create_api
import random


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, status):
        line = rand_line()
        print("answering @" + status.user.screen_name + " with : " + '@' + status.user.screen_name + ' ' + line)
        self.api.update_status(status='@' + status.user.screen_name + ' ' + line, in_reply_to_status_id=status.id)   

    def on_error(self, status):
        logger.error("Error on status", exc_info=True)


def rand_line():
    f = open('replies.txt', 'r')
    replies = f.read().splitlines()
    f.close()
    return random.choice(replies)
    

def main():
    api = create_api()
    listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, listener)
    stream.filter(track=["bora jogar bot", "escolhe pra mim bot"])

if __name__ == "__main__":
    main()