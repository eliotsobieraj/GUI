from tkinter import *
from tkinter import messagebox

def message():
    messagebox.showinfo(root,"bonjour je m'appelle turbo tanguy")
root=Tk()
Button(root,text="message",command=message).pack()



root.mainloop()