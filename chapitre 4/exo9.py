from tkinter import *


root =Tk()

for i in range(3):
    for x in range(3):
        Button(text="boutton").grid(row=i, column=x)

root.mainloop()