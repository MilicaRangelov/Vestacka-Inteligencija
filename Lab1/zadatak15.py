def izdvoji(lista):
    rez = [lista[i][i] if i < len(lista[i]) else 0 for i in range(len(lista))]
    print(rez)

def promeni(lista,x):
    rez = list(map(lambda a: a-x if a >= x else a+x , lista))
    print(rez)

izdvoji([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]])
promeni([7, 1, 3, 5, 6, 2], 3)