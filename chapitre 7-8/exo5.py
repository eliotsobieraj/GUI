from tkinter import *

root = Tk()
def pclic(*args):
    print("clic")

Button(root,text="boutton 1").pack()
Button(root,text="boutton 2").pack()
root.bind_class("Button","<Button-1>",pclic)
root.mainloop()