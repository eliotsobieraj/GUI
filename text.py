from tkinter import *

root = Tk()

text = Text(root, height=100, width=500)
text.insert(INSERT, "bonjour ....", )
text.insert(END, "Toto")
text.pack()
text.tag_add("bonjour", "1.0", "1.7")
text.tag_add("toto", "1.12", "1.16")
text.tag_config("bonjour", background="blue")
text.tag_config("toto", background="black")

root.mainloop()
