from tkinter import *

root = Tk()

btn = Button(root,text="Bonjour ! ")

btn.config(text="toto" , relief="ridge")
btn["text"] = "tata"
btn.pack()
root.mainloop()
