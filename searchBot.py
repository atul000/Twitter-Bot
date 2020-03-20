import tweepy
import time

consumer_key = 'qsm15qlNYBN9UZn9vp6yezmrU'
consumer_secret = 'z6pNLIVYXhj2C2teIuy0QVCqdwRyQ7LE0pTmBShdloS48g0m3O'

key = '988824801107152899-lEP3oG6zFsI8TUI0fc3v4vGsZoglXgC'
secret = 'mzogkCmXCA5pIUOVS6Whrctq94RFjT4wZmpvbD626sjBy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = ("datascience", "ai")
tweetNumber = 8

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)


def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            api.create_favorite(tweet.id)
            # api.update_status("Good Luck #{hashtag}", tweet.id)
            print("tweeted")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)


searchbot()
