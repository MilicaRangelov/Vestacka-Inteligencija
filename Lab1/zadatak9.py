from functools import reduce


def prosek(lista):
    pros = list(map(lambda x : reduce(lambda x,y: x+y,x) / len(x),lista))
    print(pros)

def zameni(lista, x):
    rez = [lista[i] if lista[i] > x else reduce(lambda x,y: x+y, lista[i+1:]) for i in range(len(lista))]
    print(rez)
    
prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]])    
zameni([1, 7, 5, 4, 9, 1, 2, 7], 5)
    