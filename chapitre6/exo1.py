from tkinter import *

root = Tk()
var = StringVar()
var.set("au revoir")


def callback():
    print(var.get())


Entry(root, textvariable=var).pack()
Button(root, text="envoyer", command=callback).pack()
root.mainloop()
