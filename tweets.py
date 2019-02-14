from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy
consumer_key="N7B8ZwSdv5DnUpZQJCik7e2vd"
consumer_secret="iRUY2E8jevhgHoegRRMZGyrD46cr9jWATzU0D72ea5fYmu8BHh"
access_token="804712681387290624-lFCSKZlFq7epwdPjnzsz7ByZe08FSKN"
access_token_secret="1kfYdjZfxigR8m6PZRyOkaPVMdksJZHL2JTEWzR12EfXX"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

n =str(input("give first username "))
n2 =str(input("give second username "))
names=[]
followers_list=[]
twords=[]
tsum=[]
names.append(n)
names.append(n2)
for peps in names:
    user = api.get_user(peps)
    print('Name: ' + user.name)
    print('Location: ' + user.location)
    print('Followers: ' + str(user.followers_count)+ "\n")
    followers = str(user.followers_count)
    followers_list.extend(followers)
    tweets = api.user_timeline(screen_name = user.name, count=100, incude_rts = False, tweet_mode = 'extended')

    for inf in tweets[:10]:
        print(inf.created_at)
        print(inf.full_text)
        print("\n")
        c = 0
        twords.extend(inf.full_text)
        for line in twords:
            twords=line.split(" ")
            c+= len(twords)
    print("No of words=" + str(c))
    result = int(user.followers_count)
    totresult = result * int (c)
    tsum.append(str(totresult))
    print("\n")
tsum = [int(i) for i in tsum ]
if tsum[0] > tsum[1]:
    print("the winner is:" + names[0])
else:
    print("the winner is:" + names[1])
