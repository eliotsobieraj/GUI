import tkinter as tk

root = tk.Tk()
rect_ver = tk.Canvas(height=800,width=300)

rect_ver.create_rectangle(50,40,300,400,fill="green")
rect_ver.create_line(50,40,300,400,fill="white")
rect_ver.pack()
root.mainloop()