from tkinter import *
from tkinter import messagebox

root =Tk()
var = StringVar()
def keyevent(event):
    var.set(event.char)
    messagebox.showwarning("warning",var.get())
root.bind_all("<KeyRelease>",keyevent)


root.mainloop()