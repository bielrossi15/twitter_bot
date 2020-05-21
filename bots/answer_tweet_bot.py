import tweepy
import logging
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class AnswerTweetBot(tweepy.StreamListener):
    def __init__(self,api, image_path):
        self.api = api
        self.me = api.me()
        self.image_path = image_path

    def on_status(self, status):
        if status.in_reply_to_status_id is not None or \
            status.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        print("NEW TWEET FROM @{}".format(status.user.screen_name))
        print("TWEET: {}".format(status.text))
        print("ANSWERING TWEET WITH: oi")
        self.api.update_with_media(image_path, status="@" + status.user.screen_name + "\n" +" ​| (＼  　(🎩/)      ｜   )​\n" + "ヽ　ヽ` ( ͡° ͜ʖ ͡°) _ノ    /​ \n"
        "　​＼ |　⌒Ｙ⌒　/  /​\n" + "　​｜ヽ　 ｜　 ﾉ ／ \n" + "　 ​＼トー仝ーイ \n" + "　　 ​｜ ミ土彡 |​ \n" 
        + "         ​) \      °     /​ \n" + "         ​(     \       /​l \n" + "         ​/       / ѼΞΞΞΞΞΞΞD​" + u"\U0001F4A6"
        , in_reply_to_status_id=status.id)   



api = create_api()
image_path = './Vampeta-nu.jpg'
listener = AnswerTweetBot(api, image_path)
stream = tweepy.Stream(api.auth, listener)
user1 = api.get_user(screen_name='@jairbolsonaro')
user2 = api.get_user(screen_name='@CarlosBolsonaro')
user3 = api.get_user(screen_name='@BolsonaroSP')
user4 = api.get_user(screen_name='@AbrahamWeint')

stream.filter(follow=[str(user1.id), str(user2.id), str(user3.id), str(user4.id)])