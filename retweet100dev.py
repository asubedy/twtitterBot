import tweepy
from datetime import date
from datetime import timedelta
import os
import schedule
import time

consumer_key = os.getenv('conumser_key')
consumer_secret_key = os.getenv('consumer_secret_key')
access_token = os.getenv('access_token')
access_secret_token = os.getenv('access_secret_token')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)

auth.set_access_token(access_token, access_secret_token)

api = tweepy.API(auth)

screen_name = "leonnoel"
user = api.get_user(screen_name)

_id = user.id
my_screen_name = "frexpe12"

timeline = api.user_timeline(_id, count=5)

tweet_id = 0
today = date.today()
yesterday = today - timedelta(days=1)
str_date = yesterday.strftime("%B %d, %Y")
print(str_date)

print(str_date)

print("\nThe screen name " + screen_name +
      " corresponds to the user with the name : " +
      str(user.name))

# if there is any tweet you want to retweet with specific content in it
check = "Day 6 of #100Devs"

# to identify the tweet that is to be retweeted
for status in timeline:
    if check in status.text:
        print(status.text)
        d3 = str(status.created_at.strftime("%B %d, %Y"))
        print(d3)
        if str_date == d3:
            print("Yes there is a tweet today")
            print(status.id)
            tweet_id = status.id
            break
        else:
            print("No tweet to retweet")

# finally using the twitter api to like and retweet the code;

status = api.get_status(tweet_id)
if status.favorited == False:
    api.create_favorite(tweet_id)
if status.retweeted == False:
    api.retweet(tweet_id)
favorited = status.favorited
retweeted = status.retweeted
print(favorited)
print(retweeted)


# def job():
#     print("I'm working...")

# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().wednesday.at("10:30").do(job)

# while 1:
#     schedule.run_pending()
#     time.sleep(1)
