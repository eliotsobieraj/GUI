from tkinter import *

root = Tk()
def totop(*args):
    print("toto")
def annuler(*args):
    btn1.unbind("<Button-1>", bindevent)



btn1 = Button(root,text="Toto")
btn2 = Button(root,text="annuler")
bindevent = btn1.bind("<Button-1>",totop)
bindevent2 = btn2.bind("<Button-1>",annuler)
btn1.pack()
btn2.pack()
root.mainloop()