from tkinter import *
root = Tk()
svar = StringVar()

def plabel(event):
    svar.set(event.widget["text"])

Label(root,textvariable=svar).pack()
Button(root,text="toto").pack()
Button(root,text="titi").pack()
Button(root,text="tata").pack()



root.bind_class("Button","<Button-1>",plabel)
root.mainloop()