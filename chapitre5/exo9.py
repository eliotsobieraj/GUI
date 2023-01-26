from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


root = Tk()
file = filedialog.askopenfilename()
print(file)

root.mainloop()