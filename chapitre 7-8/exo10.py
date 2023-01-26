from tkinter import *

root = Tk()
xvar = IntVar()
yvar = IntVar()


def coord(event):
    print(event.x,event.y )




root.bind_all("<Motion>", coord)

root.mainloop()
