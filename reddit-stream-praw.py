import praw
import sys
import json

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

for submission in subreddits.stream.submissions():
    try:
        if submission.selftext == '' and submission.title == '':
            continue
        json.dumps({'abc': 123, 'fcs': 'sdc'})
    except praw.exceptions.PRAWException as e:
        pass
