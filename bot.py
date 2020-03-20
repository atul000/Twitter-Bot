import tweepy
import time

consumer_key = 'qsm15qlNYBN9UZn9vp6yezmrU'
consumer_secret = 'z6pNLIVYXhj2C2teIuy0QVCqdwRyQ7LE0pTmBShdloS48g0m3O'

key = '988824801107152899-lEP3oG6zFsI8TUI0fc3v4vGsZoglXgC'
secret = 'mzogkCmXCA5pIUOVS6Whrctq94RFjT4wZmpvbD626sjBy'

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
