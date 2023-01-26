from tkinter import *

root = Tk()
num = IntVar()


def maj(*args):
    num.get()
    if num.get() == 100:
        print("toto")



num.trace("w", maj)
Scale(root, variable=num,orient="horizontal").pack()
Label(root, textvariable=num).pack()
root.mainloop()
