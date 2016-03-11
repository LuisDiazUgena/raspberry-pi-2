#!/usr/bin/python
from Tkinter import *
import Adafruit_DHT

def doNothing():
    print ("Ok, I'm going to do nothing")

root = Tk()
root.minsize(width=600, height=200)
root.maxsize(width=780,height=460)

# ***** Toolbar *****
toolBar = Frame(root,bd=1,relief=SUNKEN)

instertButton = Button(toolBar,text="About",command = doNothing)
instertButton.pack(side=LEFT,padx=2,pady=2) #add padding
printButton = Button(toolBar,text="Github repo",command = doNothing)
printButton.pack(side=LEFT,padx=2,pady=2) #add padding
quitButton = Button(toolBar,text="Quit",command = root.quit)
quitButton.pack(side=LEFT,padx=2,pady=2) #add padding
toolBar.pack(side=TOP,fill=X)

# ***** Statusbar *****
status = Label(root,text=" Preparing to do read...",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)
#"run" the main window
# ***** Frames *****
topFrame=Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
# ***** Elements *****

labelT = Label(topFrame,text="Temperature",font=("Helvetica", 25))
valueT = Label(topFrame,text="No data",font=("Helvetica", 25))
labelH = Label(bottomFrame,text="Humidity",font=("Helvetica", 25))
valueH = Label(bottomFrame,text="No data",font=("Helvetica", 25))

labelT.pack(side=LEFT)
valueT.pack(side=LEFT)
labelH.pack(side=LEFT)
valueH.pack(side=LEFT)

root.mainloop()

sensor = Adafruit_DHT.DHT22
pin=21
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
    	print 'Temp={0:0.1f}C  Humidity={1:0.1f}%'.format(temperature, humidity)
    else:
    	print 'Failed to get reading. Try again!'
