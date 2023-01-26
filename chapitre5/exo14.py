from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser

root = Tk()

color = colorchooser.askcolor(color="#00ff00",title="color chooser")
root.config(bg=color[1])

root.mainloop()
