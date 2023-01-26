from tkinter import *


def close(*args):
    root.destroy()


root = Tk()

btn = Button(root, text="cliquez")
btn.bind("<Button-2>", close)
btn.pack()
root.mainloop()
