from tkinter import *

root =Tk()
bool = BooleanVar()
def activate():
    print(bool.get())
    if bool.get() is True:
        global btn
        btn.config(state=NORMAL)
    else:
        btn.config(state = DISABLED)



checkbtn = Checkbutton(root,text="check",variable=bool,command=activate).pack()
btn = Button(root, text="activatebutton",state=DISABLED)

btn.pack()
root.mainloop()
