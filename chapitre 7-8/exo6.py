from tkinter import *

root = Tk()

def validate(event):
    result = event.char
    if result.isnumeric():
        print("validate")
    else:
        print("invalidate")
        event.widget.delete(0,END)

Entry(root).pack()
Entry(root).pack()
root.bind_class("Entry","<KeyRelease>",validate)
root.mainloop()