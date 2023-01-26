from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


root = Tk()
tabnaems =filedialog.askopenfilenames()
print(tabnaems)
root.mainloop()