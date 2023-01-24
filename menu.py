import tkinter as tk

root = tk.Tk()

menuBtn = tk.Menubutton(root,text="Menu")
menuBtn.menu = tk.Menu(menuBtn)
menuBtn["menu"] = menuBtn.menu

var = tk.StringVar()
def printvartoto():
    print("toto")
def printvartata():
    print("tata ")

menuBtn.menu.add_checkbutton(label="toto",variable=var,command=printvartoto)
menuBtn.menu.add_checkbutton(label="tata",variable=var,command=printvartata)
menuBtn.pack()
root.mainloop()