from tkinter import *

root = Tk()

img=PhotoImage(file='image2.png')

Label(root,image=img).pack(side=LEFT)

Button(root,text="button").pack(side=RIGHT)

root.mainloop()