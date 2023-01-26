from tkinter import *

root = Tk()

def newfen():
    global fenetre
    fenetre = Toplevel(root)

    fenetre.grab_set()

    Button(fenetre,text="fermer",command=fermeture).pack()
    Label(fenetre,text="veuillez patienter ...").pack()
    root.wait_window(fenetre)
    print("toto")


def fermeture():
    fenetre.destroy()

boutton = Button(root,text="ouvrir une nouvelle fenetre",command=newfen).pack()








root.mainloop()