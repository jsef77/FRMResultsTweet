import tkinter as tk
from tweet import *
import ast

#Twitter Handle Dictionaries

playerHandlesFile = open('players.txt', 'r').read()
playerHandles = ast.literal_eval(playerHandlesFile)

# Update button function

def formatPlayer(player, character):
    if player.lower() in playerHandles:
        if character == "":
            character = playerHandles.get(player.lower())[1]
        player = playerHandles.get(player.lower())[0]

def updateTweet(date, p1, p1Char, p2, p2Char, p3, p3Char, p4, p4Char, artist):

    # Name & Character replace

    formatPlayer(p1, p1Char)
    formatPlayer(p2, p2Char)
    formatPlayer(p3, p3Char)
    formatPlayer(p4, p4Char)
    
    if artist.lower() in playerHandles:
        artist = playerHandles.get(artist.lower())[0]

    #Tweet Preview
    global preTweet

    preTweet = ("Results from this week!\n{}\n\n1st: {} ({})\n2nd: {} ({})\n3rd: {} ({})\n4th: {} ({}) \n\nartwork courtesy of {}").format(date, p1, p1Char, p2, p2Char, p3, p3Char, p4, p4Char, artist)

    if len(preTweet) < 280:
        print(preTweet)
    else:
        print("@@@@@@  ERROR: TWEET TOO LONG  @@@@@@") 

def preTweetSend(date, p1, p1Char, p2, p2Char, p3, p3Char, p4, p4Char, artist):

    global preTweet
    
    if len(preTweet) < 280:
        print("TWEETING...\n")
        tweetSend(date, preTweet)
    else:
        print("@@@@@@  ERROR: TWEET TOO LONG  @@@@@@\n@@@@@@ NOTHING SENT @@@@@@") 
