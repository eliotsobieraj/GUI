from tkinter import *
root = Tk()
num = IntVar()
num2 = IntVar()

def callback(*args):
    num.set(num2.get())

num2.trace("w",callback)
Spinbox(root,textvariable=num2,from_=0,to=100).pack()
Scale(root,variable=num,orient="horizontal").pack()
root.mainloop()
