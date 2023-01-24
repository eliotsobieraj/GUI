import tkinter as tk

root = tk.Tk()
v = tk.StringVar(root,"eliott")

label = tk.Label(root,textvariable=v)

label.pack()

root.mainloop()
