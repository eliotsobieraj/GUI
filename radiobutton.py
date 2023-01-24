import tkinter as tk


def printvaluea():
    print("vous avez selectionné :" + var_str.get())


root = tk.Tk()
var_str = tk.StringVar()
button = tk.Radiobutton(root, text="a", value="yooh", variable=var_str, command=printvaluea)
button2 = tk.Radiobutton(root,text="variable",value="ceci n'est pas une variable",variable=var_str,command=printvaluea)
button2.pack(anchor=tk.E)
button.pack(anchor=tk.W)
root.mainloop()

