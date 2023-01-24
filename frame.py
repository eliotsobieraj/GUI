import tkinter as tk

root= tk.Tk()

frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP)
frame2 = tk.Frame(root)
frame2.pack(side = tk.BOTTOM)

v1 = tk.StringVar(root,"Toto")
v2 = tk.StringVar(root,"Tata")

label1 = tk.Label(frame1,textvariable=v1)
label2 = tk.Label(frame2,textvariable=v2)
label1.pack()
label2.pack()

root.mainloop()