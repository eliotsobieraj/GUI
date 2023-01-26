from tkinter import *

root = Tk()
def bgchange(event):
    event.widget.config(bg="red")

Label(root,width=100,height=10,text="label",borderwidth=2,relief="solid").pack()
Label(root,width=100,height=10,text="label",borderwidth=2,relief="solid").pack()




root.bind_class("Label","<Double-Button-1>",bgchange)


root.mainloop()