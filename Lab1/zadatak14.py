from functools import reduce


def unija(l1,l2):
    rez = list(filter(lambda x: x not in l1 ,l2))
    l1.extend(rez)
    print(l1)

def suma(lista):
    rez = [reduce(lambda x,y: x+y, lista[i]) for i in range(len(lista))]
    print(rez)

unija([5, 4, "1", "8", 3, 7], [1, 9, "1"])    
suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]])