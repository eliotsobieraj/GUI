from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


root = Tk()
name = filedialog.askopenfilename()
open(name,"w",encoding="utf8")
root.mainloop()