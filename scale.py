from tkinter import *

root = Tk()


def list_num():
    list_val = 'value = ' + str(var.get())
    label.config(text=selected)

def printval():
    print(f"scale value is : {int(var.get())}")

var = DoubleVar()
s = Scale(root,from_=0,to=10,variable=var)
s.pack(anchor=CENTER)
btn = Button(root,command=printval,text="button")
btn.pack(anchor=W)


label = Label(root)
label.pack()
root.mainloop()
