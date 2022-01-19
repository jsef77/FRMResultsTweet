from tweet import *
from buttonfunc import *
import tkinter as tk

debug = False    

window = tk.Tk()

entryDate = tk.Entry()
entryP1 = tk.Entry()
entryP2 = tk.Entry()
entryP3 = tk.Entry()
entryP4 = tk.Entry()
entryArtist = tk.Entry()

entryP1Char = tk.Entry()
entryP2Char = tk.Entry()
entryP3Char = tk.Entry()
entryP4Char = tk.Entry()

# Entries Rendered to Window

lrx = 2

labelBlank = tk.Label()

labelChars = tk.Label(text="Character(s) (x/y/z)").grid(row=0, column=2)

labelP1 = tk.Label(text="P1:").grid(row=lrx+2, column=0)
labelP2 = tk.Label(text="P2:").grid(row=lrx+3, column=0)
labelP3 = tk.Label(text="P3:").grid(row=lrx+4, column=0)
labelP4 = tk.Label(text="P4:").grid(row=lrx+5, column=0)

labelArt = tk.Label(text="Artwork by:").grid(row=lrx+7, column=1)

erx = lrx

entryDate.insert(0, "dd/mm/yy")
entryDate.grid(row=0, column=1)

entryP1.grid(row=erx+2, column=1)
entryP2.grid(row=erx+3, column=1)
entryP3.grid(row=erx+4, column=1)
entryP4.grid(row=erx+5, column=1)

entryP1Char.grid(row=erx+2, column=2)
entryP2Char.grid(row=erx+3, column=2)
entryP3Char.grid(row=erx+4, column=2)
entryP4Char.grid(row=erx+5, column=2)

## PADDING ##
labelBlank.grid(row=erx+6, column=1, columnspan=3)
## PADDING ##

entryArtist.grid(row=erx+7, column=2)

#Function calls

def entryUpdate():

    global date
    global p1
    global p2
    global p3
    global p4
    global p1Char
    global p2Char
    global p3Char
    global p4Char
    global artist

    date = entryDate.get()
    p1 = entryP1.get()
    p2 = entryP2.get()
    p3 = entryP3.get()
    p4 = entryP4.get()
    p1Char = entryP1Char.get()
    p2Char = entryP2Char.get()
    p3Char = entryP3Char.get()
    p4Char = entryP4Char.get()
    artist = entryArtist.get()
    
    

def updateCall():
    
    entryUpdate()

    updateTweet(date, p1, p1Char, p2, p2Char, p3, p3Char, p4, p4Char, artist, debug)

    

def tweetCall():

    entryUpdate()

    preTweetSend(date, p1, p1Char, p2, p2Char, p3, p3Char, p4, p4Char, artist, debug)

    
#Buttons
buttonUp = tk.Button(
    text="update & preview",
    bg="green",
    fg="white",
    command=updateCall
)

buttonTweet = tk.Button(
    text="Tweet!",
    bg="blue",
    fg="white",
    command=tweetCall
)
# Buttons Rendered to Window

buttonUp.grid(row=998, column=3)
buttonTweet.grid(row=999,column=3)

##############################

window.mainloop()


