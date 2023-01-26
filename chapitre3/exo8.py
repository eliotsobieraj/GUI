from tkinter import *

root = Tk()


canv = Canvas(root,height=100,width=200)
canv.create_line(200,20,50,50,150,60,200,20,width=10,joinstyle="miter")


canv.pack()
root.mainloop()