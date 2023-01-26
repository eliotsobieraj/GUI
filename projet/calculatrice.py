from tkinter import *

root = Tk()

num1 = StringVar()
num1.set("")
num2 = StringVar()
root.config(width=286,height=387)
sign= StringVar()
affich=StringVar()

def ajouter(event):
    if event.widget["text"] in "1234567890":
        affich.set(affich.get()+event.widget["text"])
    elif  event.widget["text"] in "+-/x":
        if num1.get() == "":
            num1.set(affich.get())
        sign.set(event.widget["text"])
        affich.set("")
        print(sign.get())
    elif event.widget["text"] in "=":
        num2.set(affich.get())
        if num1.get() != "" and num2.get() != "" and sign.get()in "+":
            affich.set(int(num1.get())+int(num2.get()))
        if num1.get() != "" and num2.get() != "" and sign.get()in "-":
            affich.set(int(num1.get())-int(num2.get()))
        if num1.get() != "" and num2.get() != "" and sign.get() in "x":
            affich.set(int(num1.get()) * int(num2.get()))
        if num1.get() != "" and num2.get() != "" and sign.get() in "/":
            if int(num2.get()) != 0:
                affich.set(int(num1.get()) / int(num2.get()))
            else :
                affich.set("ERROR")
    elif event.widget["text"] in "C":
        num1.set("")
        num2.set("")
        affich.set("")


ecran = Label(root,anchor=E,textvariable=affich,width=14,height=1,bg="black",fg="white",font=("arial", 24))
bnt1 = Button(root,text="1",padx=40,pady=20,bg="#E6E6FA").grid(row=1,column=0)
bnt2 = Button(root,text="2",padx=40,pady=20,bg="#E6E6FA").grid(row=1,column=1)
bnt3 = Button(root,text="3",padx=40,pady=20,bg="#E6E6FA").grid(row=1,column=2)
bnt4 = Button(root,text="4",padx=40,pady=20,bg="#E6E6FA").grid(row=2,column=0)
bnt5 = Button(root,text="5",padx=40,pady=20,bg="#E6E6FA").grid(row=2,column=1)
bnt6 = Button(root,text="6",padx=40,pady=20,bg="#E6E6FA").grid(row=2,column=2)
bnt7 = Button(root,text="7",padx=40,pady=20,bg="#E6E6FA").grid(row=3,column=0)
bnt8 = Button(root,text="8",padx=40,pady=20,bg="#E6E6FA").grid(row=3,column=1)
bnt9 = Button(root,text="9",padx=40,pady=20,bg="#E6E6FA").grid(row=3,column=2)
bnt0 = Button(root,text="0",padx=40,pady=20,bg="#E6E6FA").grid(row=4,column=0)
bntp = Button(root,text="+",padx=40,pady=20,bg="#a6a6ed").grid(row=4,column=1)
bntm = Button(root,text="-",padx=40,pady=20,bg="#a6a6ed").grid(row=4,column=2)
bntf = Button(root,text="x",padx=40,pady=20,bg="#a6a6ed").grid(row=5,column=0)
bntd = Button(root,text="/",padx=40,pady=20,bg="#a6a6ed").grid(row=5,column=1)
bnte = Button(root,text="=",padx=40,pady=20,bg="#a6a6ed").grid(row=5,column=2)
bntC = Button(root,text="C",padx=134,pady=20,bg="#fae6e6").grid(row=6,column=0,columnspan=3)


root.bind_class("Button","<Button-1>",ajouter)


ecran.grid(row=0,column=0,columnspan=3)
root.resizable(False,False)
root.mainloop()