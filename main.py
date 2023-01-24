import random


# print(12+5)
# first_name = "eliott"
# print(first_name)
# nom = input("entrez nom  : ")
# prenom = input("entrez prenom  : ")
# age = input("entrez age  : ")

# print(f"bonjour {prenom} vous avez {age}ans")
# nombre = int(input("entrez un nombre : "))
# print(2*nombre)
# tab = [0, 1, 2, 4, 8, 16]
# print(tab[3])

# age = int(input("entrez votre age : "))
# if age>=18 :
# print(" vous etes majeur")
# else :
# print("vous etes mineur")

# liste= ["bob", "alice", "patrick"]
# prenom= input("entrez votre prenom : ")
# if prenom in liste :
#    print("acces autorise ")
# else :
#   print(" acces refusé")
# for i in range(101):
#   print(i)

def boucle():
    rep = "N"
    while rep == "N":
        print("Ceci n'est pas une boucle.")
        rep = input("Voulez-vous ne plus revoir ce message [Y/N] :")
        if rep == "Y":
            return "fin de la boucle"
        elif rep == "N":
            pass
        else:
            print("je n'ai pas compris ce que vous avez rentré : ")
            rep = "N"


def fizzbuzz():
    for i in range(100):

        if i % 3 == 0 and i % 5 == 0 and i > 1:
            print("fizzbuzz")
        elif i % 3 == 0 and i > 1:
            print("fizz")
        elif i % 5 == 0 and i > 1:
            print("buzz")
        else:
            print(i)


def prenom(name):
    print(f"hello {name}")


def list_pair(n):
    tab = []
    for i in range(0, n - 1, 2):
        tab.append(i)
    return tab


def tab_mul(x):
    for i in range(1, 11):
        print(f"{i} * {x} = {i * x}")


def tab_valeur():
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


def tab_memo():
    values1 = None
    values2 = None
    x_values = 0
    y_value = 2
    count = 20
    tab_val = tab_valeur()
    line = []
    tab = []
    for x in range(5):
        line.append("?")
    for i in range(4):
        tab.append(line)

    while "?" in tab[0]:
        y_values = int(input("entrez l'index y de votre premiere valeur"))
        x_values = int(input("entrez l'index x de votre premiere valeur"))
        values1 = [x_values, y_values]
        y_values = int(input("entrez l'index y de votre premiere valeur"))
        x_values = int(input("entrez l'index x de votre premiere valeur"))
        values2 = [x_values, y_values]
        tab[values1[0], values1[1]] = tab_val[values1[0], values1[1]]
    for i in range(4):
        print(' '.join(tab[i]))


# print(boucle())
# fizzbuzz()
# print(list_pair(10))
# print(tab_mul(3))
tab_memo()
print(tab_valeur())
