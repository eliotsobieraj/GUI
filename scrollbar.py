from tkinter import *

root = Tk()

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)


liste = Listbox(root, yscrollcommand=scroll.set)
for i in range(1,100):
    liste.insert(END,str(i)+" -BONJOUR")

liste.pack(side=LEFT, fill=BOTH)
scroll.config(command=liste.yview)


root.mainloop()