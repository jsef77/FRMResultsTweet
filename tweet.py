import tkinter as tk
from twython import Twython
from auth import *

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )


#Actual Tweet
def tweetSend(imageName, preTweet):

    imageName = 'img/' + imageName.replace("/", ".") + '.png'
    
    message = preTweet
    image = open(imageName, 'rb')
    response = twitter.upload_media(media=image)
    media_id = [response['media_id']]
    
    twitter.update_status(status=message, media_ids=media_id)
    print("Tweeted!")
