import tkinter as tk


root = tk.Tk()

def bonjout():
    print("bonjour")

btn = tk.Button(root,text ="cliquez ici!", command= bonjout)
btn.pack()
root.mainloop()