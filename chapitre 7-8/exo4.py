from tkinter import *

root = Tk()


def bjr(*args):
    print("bonjour")


root.bind_all("<KeyPress-b>",bjr)

root.mainloop()
