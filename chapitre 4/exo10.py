from tkinter import *

root = Tk()


Label(text="label",bg="red").grid(row=0,column=0,sticky='nsew')
Button(text="button",bg="red", relief='groove').grid(row=1,column=0,sticky='nsew')
Entry(bg="red").grid(row=3,column=0,sticky='nsew')


root.columnconfigure(0,weight=1)
root.mainloop()
