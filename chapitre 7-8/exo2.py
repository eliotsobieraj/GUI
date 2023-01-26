from tkinter import *

root = Tk()

def change_color(*args):
    frm.config(bg="red")
    print("toto")
def leave(*args):
    frm.config(bg="blue")
frm = Frame(root,height=100,width=200,bg="blue")
frm.bind("<Enter>",change_color)
frm.bind("<Leave>",leave)
frm.pack()
root.mainloop()