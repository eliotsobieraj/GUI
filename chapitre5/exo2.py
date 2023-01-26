from tkinter import *

root = Tk()


def newfen():
    global newfenetre
    newfenetre = Toplevel(root)
    btn2 = Button(newfenetre,text="minimise",command=minimise).pack()
    btn3= Button(root,text="restaure",command=resto).pack()


def minimise():
    newfenetre.iconify()

def resto():
    newfenetre.deiconify()


Button(root, text="new", command=newfen).pack()
btnresto= Button(root)
root.mainloop()