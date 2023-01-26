from tkinter import *
import tkinter.font

root = Tk()
lab2font= tkinter.font.Font(family = 'arial', overstrike ='1')

lab1 = Label(root,text="Toto", font='arial 14 underline')
lab2 = Label(root,text="tata",font=lab2font )
lab3 = Label(root,text = 'titi', font=('bold'))


lab1.pack()
lab2.pack()
lab3.pack()

root.mainloop()