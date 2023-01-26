from tkinter import *

root = Tk()
root.config(height=500 , width=500)
list = Listbox(root)

list.insert(1,"bonjour")
Button(root,text="button").pack(side=RIGHT, anchor=CENTER)

list.pack(side= LEFT)

root.mainloop()