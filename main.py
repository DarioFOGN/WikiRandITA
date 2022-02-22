import re
from tkinter import ttk
import tkinter.messagebox
from tkinter import *
import webbrowser as web
import random as rand
import requests as req


def main():
    #reading the file
    links = []
    r = open("links.txt", "r")

    for line in r:
        links.append(line)

    win=Tk() #creating the main window and storing the window object in 'win'
    win.title('WikiRand') #setting title of the window
    win.geometry('300x250') #setting the size of the window
    win.attributes('-topmost', True) #setting the maximize to false

    win.resizable(0,0)

    #function of the button, it will get a random link in lists and open it for you when you'll press the button    
    def func():
            url = "https://it.wikipedia.org" + links[rand.randint(0,len(links))]
            web.open_new_tab(url)

    #functions to declare window objects and position
    btn=Button(win,text="Nuovo link", width=10,height=2,command=func)
    btn.place(x=110,y=90)
    win.mainloop() #running the loop that works as a trigger

    #req.
    return 0

if __name__=="__main__":
    main()
