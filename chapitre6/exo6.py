from tkinter import *

root = Tk()

svar = StringVar()
svar.set("tata")


def change():
    svar.set("toto")


Button(root, text="change", command=change).pack()
Label(root, textvariable=svar).pack()

root.mainloop()
