import re
import praw
import config
import time

def bot_login():
    print ("Loggin in...")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent ="Yourname's Cat comment responder v0.1")
    print ("Logged in!")

    return r 

def run_bot(r):
    print ("Obtaining 25 comments...")
    for comment in r.subreddit ('Subreddit name').comments(limit=25):
        if "cat" in comment.body:
            print ("String with \"cat\" found in comment")
            comment.reply("yes we're >cute< (https://i.pinimg.com/236x/8e/2d/33/8e2d33848b159f3d325e0bbd45471f82.jpg)")
            print ("Replied to comment")

    print ("Sleeping for 10 seconds...")
    #Sleep for 10 seconds...
    time.sleep(10)



r = bot_login()
run_bot(r)
