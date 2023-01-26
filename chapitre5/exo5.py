from tkinter import *
from tkinter import messagebox
root = Tk()


message =messagebox.askyesno(root,"etes vous majeur")
if message is True:
    print("yes")
else:
    print("No")

root.mainloop()