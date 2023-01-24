import random


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
    xval, yval = 0, 0
    xval = int(input("entrez le x de la veleur"))
    yval = int(input("entrez le y de la valeur"))
    values1 = [yval,xval]
    xval = int(input("entrez le x de la veleur"))
    yval = int(input("entrez le y de la valeur"))
    values2 = [yval, xval]
    if tab_val[values1[0]][values1[1]] == tab_val[values2[0]][values2[1]]:
        print("")



memo_main()