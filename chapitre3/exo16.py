from tkinter import *

root = Tk()
img = PhotoImage(file='image2.png')
label = Label(root,image=img)


label.pack()
root.mainloop()
