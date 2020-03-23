import tweepy
import time

consumer_key = '__Your Consumer Key__'
consumer_secret = '__your consumer_secret__'

key = 'key'
secret = 'secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


FILE_NAME = 'last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


tweets = api.mentions_timeline(
    read_last_seen(FILE_NAME), tweet_mode='extended')


def reply():
    for tweet in reversed(tweets):
        if '#RandomTweet' in tweet.full_text:
            print("Replied to ID - " + str(tweet.id))
            api.update_status("@" + tweet.user.screen_name +
                              " Good Luck For #100DaysOfCode", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


while True:
    reply()
    time.sleep(15)
