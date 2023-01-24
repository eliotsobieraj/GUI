import tkinter as tk

root = tk.Tk()
v = tk.StringVar(root,"toto")

liste = tk.Listbox(root)
liste.insert(1,"toto")
liste.insert(2,"tata")

liste.pack()
root.mainloop()