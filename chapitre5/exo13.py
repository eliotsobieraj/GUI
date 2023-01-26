from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


root = Tk()
files = filedialog.askopenfilename(filetypes=[("md files", "*.md")])
f= open(files,"r",encoding="utf8")
print("".join(f.readlines()))

root.mainloop()
f.close()
