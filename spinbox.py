from tkinter import *

def printvar():
    print(var.get())

root = Tk()
var = StringVar()
spinbox = Spinbox(root,from_=0, to=10,textvariable=var)
button = Button(root, text="button", command=printvar)
spinbox.pack()
button.pack(side=LEFT)
root.mainloop()