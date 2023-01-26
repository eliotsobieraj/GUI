from tkinter import *
from tkinter import filedialog

from tkinter import messagebox


root = Tk()

folder = filedialog.askdirectory()

print(folder)

root.mainloop()