from tkinter import *
from tkinter import messagebox

root = Tk()
def ferm():
    message = messagebox.askyesno("fermeture","voulez vous fermer la fenetre")
    if message is True:
        root.destroy()

Button(root,text="fermer ", command=ferm).pack()

root.mainloop()