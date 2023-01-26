

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser


root = Tk()

lbl= Label(root,text="text color ....",fg="black")
color=colorchooser.askcolor(color="green",title="color chooser")
lbl.config(fg=str(color[1]))
lbl.pack()
root.mainloop()