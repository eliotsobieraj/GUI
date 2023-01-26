from tkinter import *

root = Tk()
var = StringVar()
var.set("bonjour")
Label(root,textvariable=var).pack()
Entry(root,textvariable=var).pack()
root.mainloop()