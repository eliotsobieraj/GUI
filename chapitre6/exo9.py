from tkinter import *

root = Tk()
svar = StringVar()
svar.set("toto")


def maj(*args):
    svar.get() 

def reset():
    svar.set("")


svar.trace("w", maj)

Label(root, textvariable=svar).pack()
Label(root, textvariable=svar).pack()
Label(root, textvariable=svar).pack()
Button(root,text="reset",command=reset).pack()
root.mainloop()
