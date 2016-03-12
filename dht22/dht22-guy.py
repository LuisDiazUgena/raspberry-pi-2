#!/usr/bin/python
from Tkinter import *
import tkMessageBox
import tkFont
import webbrowser
import threading
import time

def doNothing():
    print ("Ok, I'm going to do nothing")
def about():
    tkMessageBox.showinfo("About","App developed by Luis Diaz")
def openGit():
    url="https://github.com/LuisDiazUgena/raspberry-pi-2/tree/master/dht22"
    webbrowser.open(url, new=2, autoraise=True)
def measure():
    print("Let's get some data!")

class App:

    def __init__(self,_master):
        # ***** Toolbar *****
        self.toolBar = Frame(_master,bd=1,relief=SUNKEN)
        # ***** Statusbar *****
        self.status = Label(_master,text=" Preparing to do read...",bd=1,relief=SUNKEN,anchor=W)
        # ***** Buttons to bars *****
        self.aboutButton = Button(self.toolBar,text="About",command = about)
        self.githubButton = Button(self.toolBar,text="Github repo",command = openGit)
        self.quitButton = Button(self.toolBar,text="Quit",command = root.quit)
        # ***** Pack buttons *****
        self.aboutButton.pack(side=LEFT,padx=2,pady=2) #add padding
        self.githubButton.pack(side=LEFT,padx=2,pady=2) #add padding
        self.quitButton.pack(side=RIGHT,padx=2,pady=2) #add padding
        self.toolBar.pack(side=TOP,fill=X)
        self.status.pack(side=BOTTOM,fill=X)
        # ***** Frames for labels *****
        self.topFrame = Frame(_master)
        self.bottomFrame = Frame(_master)
        self.topFrame.pack(side=TOP)
        self.bottomFrame.pack(side=BOTTOM)
        # ***** Labels *****
        self.customFont = tkFont.Font(family="Helvetica", size=20)
        labelT = Label(self.topFrame,text="Temperature",font=self.customFont)
        valueT = Label(self.topFrame,text="None",font=self.customFont)
        labelH = Label(self.bottomFrame,text="Humidity",font=self.customFont)
        valueH = Label(self.bottomFrame,text="None",font=self.customFont)
        # ***** Pack labels *****
        labelT.pack(side=LEFT)
        valueT.pack(side=LEFT)
        labelH.pack(side=LEFT)
        valueH.pack(side=LEFT)
        measure()

root = Tk()
root.title("DHT22")
root.minsize(width=600, height=200)
root.maxsize(width=780,height=460)
myApp = App(root)

root.mainloop()
