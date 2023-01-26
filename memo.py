import random
import os

def affichage(tab):
    for i in range(len(tab)):
        print(" ".join(tab[i]))

def tab_secret():
    tab = []
    line=[]
    for i in range(4):
        line=[]
        for x in range(5):
            line.append("?")
        tab.append(line)
    return tab


def memo_table():
    line = []
    tab = []
    list_num = list("00112233445566778899")
    random.shuffle(list_num)
    while len(list_num) > 0:
        line = []
        for i in range(5):
            line.append(list_num.pop(0))
        tab.append(line)
    return tab


def memo_main():
    tab_val = memo_table()
    count = 20


    tab_sec= tab_secret()

    xval, yval = 0, 0
    affichage(tab_val)

    while count >0:
        os.system("cls")
        xval = int(input("entrez le x de la veleur"))
        yval = int(input("entrez le y de la valeur"))
        values1 = [yval,xval]
        xval = int(input("entrez le x de la veleur"))
        yval = int(input("entrez le y de la valeur"))
        values2 = [yval, xval]
        if tab_val[int(values1[0])][int(values1[1])] == tab_val[int(values2[0])][int(values2[1])]:
            tab_sec[values1[0]][values1[1]] = tab_val[values1[0]][values1[1]]
            tab_sec[values2[0]][values2[1]] = tab_val[values2[0]][values2[1]]
            affichage(tab_sec)






memo_main()