import re
import praw
import config
import time

def bot_login():
    print ("Loggin in...")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,import re
import praw
import config
import time
import os

def bot_login():
    print ("Loggin in...")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent ="yourname's Cat comment responder v1.1")
    print ("Logged in!")

    return r 

def run_bot(r, commnets_replied_to):
    print ("Obtaining 25 comments...")

    for comment in r.subreddit ('subreddit name').comments(limit=25):
        if "cat" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print ("String with \"cat\" found in comment: " + comment.id)
            comment.reply("yes we're >cute< (https://i.pinimg.com/236x/8e/2d/33/8e2d33848b159f3d325e0bbd45471f82.jpg)")
            print ("Replied to comment")

            comments_replied_to.append(comment.id)

            with open ("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n" )

    print (comments_replied_to) 

    print ("Sleeping for 10 seconds...")
    #Sleep for 10 seconds...
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open ("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list (filter(None, comments_replied_to))
            

    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments ()
print (comments_replied_to)

while True:

    run_bot(r, comments_replied_to)
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
