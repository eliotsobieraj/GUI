from tkinter import *

root = Tk()


Button(root,text="boutton").pack(side=LEFT, anchor=CENTER)
Entry(root).pack(anchor=CENTER)
Listbox(root).pack(side=RIGHT,anchor=CENTER)

root.mainloop()