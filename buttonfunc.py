import tkinter as tk
from tweet import *
import ast

#Twitter Handle Dictionaries

playerHandlesFile = open('players.txt', 'r').read()
playerHandles = ast.literal_eval(playerHandlesFile)

# Update button function

def updateTweet(date, p1, p1Char, p2, p2Char, p3, p3Char, p4, p4Char, artist, debug):

    # Name & Character replace

    if p1.lower() in playerHandles:
        if p1Char == "":
            p1Char = playerHandles.get(p1.lower())[1]
        p1 = playerHandles.get(p1.lower())[0]                
        if debug == True:
            print("P1 UPDATED")

    if p2.lower() in playerHandles:
        if p2Char == "":
            p2Char = playerHandles.get(p2.lower())[1]
        p2 = playerHandles.get(p2.lower())[0]
        if debug == True:
            print("P2 UPDATED")

    if p3.lower() in playerHandles:
        if p3Char == "":
            p3Char = playerHandles.get(p3.lower())[1]
        p3 = playerHandles.get(p3.lower())[0]
        if debug == True:
            print("P3 UPDATED")

    if p4.lower() in playerHandles:
        if p4Char == "":
            p4Char = playerHandles.get(p4.lower())[1]
        p4 = playerHandles.get(p4.lower())[0]
        if debug == True:
            print("P4 UPDATED")

    if artist.lower() in playerHandles:
        artist = playerHandles.get(artist.lower())[0]
        if debug == True:
            print("ARTIST UPDATED")

    #Tweet Preview
    global preTweet
    
    if debug == True:
        print("\n")
        
    preTweet = ("Results from this week!\n{}\n\n1st: {} ({})\n2nd: {} ({})\n3rd: {} ({})\n4th: {} ({}) \n\nartwork courtesy of {}").format(date, p1, p1Char, p2, p2Char, p3, p3Char, p4, p4Char, artist)

    if len(preTweet) < 280:
        print(preTweet)
    else:
        print("@@@@@@  ERROR: TWEET TOO LONG  @@@@@@") 
     
    if debug == True:
       print("------------------TWEET FIN------------------")


def preTweetSend(date, p1, p1Char, p2, p2Char, p3, p3Char, p4, p4Char, artist, debug):

    global preTweet
    
    if len(preTweet) < 280:
        print("TWEETING...\n")
        tweetSend(date, preTweet)
    else:
        print("@@@@@@  ERROR: TWEET TOO LONG  @@@@@@\n@@@@@@ NOTHING SENT @@@@@@") 
