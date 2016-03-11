from Tkinter import *

def doNothing():
    print ("Ok, I'm going to do nothing")

root = Tk()
root.title("Ras(pi)2 Commander")
#create menu item 1
mainMenu = Menu(root)
root.config(menu=mainMenu) #Make Tkinter know that mainMenu is actually a menu
root.minsize(width=600, height=200)
root.maxsize(width=780,height=460)
#Create a fileMenu
fileMenu = Menu(mainMenu)
#Add dropdown menu a.k.a cascade
mainMenu.add_cascade(label="File", menu=fileMenu)
#Now, the dropdown is empty, let's add some items
fileMenu.add_command(label="Choose version...",command = doNothing)
#add a separator
fileMenu.add_separator()
#add quit button
fileMenu.add_command(label="Quit",command=root.quit)

#create menu item 2
aboutMenu = Menu(mainMenu)
mainMenu.add_cascade(label="About", menu=aboutMenu)
aboutMenu.add_command(label="Github",command=doNothing)
aboutMenu.add_command(label="About",command=doNothing)
#"run" the main window
root.mainloop()
