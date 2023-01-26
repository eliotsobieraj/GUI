from tkinter import *

root = Tk()

svar = StringVar()
def maj(*args):
    svar.get()
svar.trace("w",maj)

Entry(root,textvariable=svar).pack()
Label(root,textvariable=svar).pack()
Label(root,textvariable=svar).pack()
Label(root,textvariable=svar).pack()

root.mainloop()