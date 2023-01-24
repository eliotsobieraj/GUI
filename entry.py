import tkinter as tk



root = tk.Tk()
v = tk.StringVar(root,"tata")
entry = tk.Entry(root,textvariable=v)
entry.pack()


root.mainloop()