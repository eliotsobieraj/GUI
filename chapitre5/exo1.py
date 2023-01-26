from tkinter import *

root = Tk()

tp = Toplevel(root)
tp.title("titre")

def destroy():
    Button.destroy(tp)


btn = Button(root, text="boutton", command=destroy)

btn.pack()

root.mainloop()
