from tkinter import *

root = Tk()
root.config(width=500,height=300)
Button(root,text="boutton").pack()
scroll = Scrollbar(root,orient="horizontal")

scroll.pack(fill="x")
root.mainloop()