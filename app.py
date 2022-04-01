import tkinter as tk
from instascrape import *
from matplotlib.pyplot import text
from sendmsg import sendmsg

def getinfo():
    profile = Profile("https://www.instagram.com/riiidhs")
    profile.scrape()
    follower = profile.followers
    print(follower)
    following = profile.following
    bio = profile.biography
    label.config(text= f"Followers={follower}\n Following={following}\n Biography={bio}\n")
    retarray = [follower, following, bio]
    return retarray
    
canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("Follow Checker")

button = tk.Button(canvas, font=24, text='Reload', command=getinfo)
button.pack(pady= 20)

sendbtn = tk.Button(canvas, font=24, text='send', command=sendmsg)
sendbtn.pack(pady= 20)

label = tk.Label(canvas, font=18,justify="left")
label.pack(pady= 20)

canvas.mainloop()
sendmsg(getinfo())
