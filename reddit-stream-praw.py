import praw
from pymongo import MongoClient
import sys

client_id = sys.argv[1]
client_secret = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
user_agent = sys.argv[5]

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

subreddits = reddit.subreddit('all')

client = MongoClient('localhost', 27017)
db = client['reddit']
col = db['reddit']

count = 0
for submission in subreddits.stream.submissions():
    try:
        if submission.selftext == '' and submission.title == '':
            continue
        dict = {
            'subreddit': submission.subreddit.display_name,
            'selftext': submission.selftext,
            'author_fullname': submission.author_fullname,
            'title': submission.title,
            'name': submission.name,
            'created': submission.created,
            'subreddit_id': submission.subreddit_id,
            'id': submission.id,
            'permalink': submission.permalink,
            'url': submission.url,
            'created_utc': submission.created_utc,
            'soda_source': 'praw_streaming'
        }
        col.insert_one(dict)
    except praw.exceptions.PRAWException as e:
        pass
