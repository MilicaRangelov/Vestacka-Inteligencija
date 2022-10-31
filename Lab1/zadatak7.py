from functools import reduce
from pickle import NONE


def operacija(lista, fja):
    rez = [reduce(fja,el) for el in lista]
    print(rez)

def objedini(A:list):
    #ne radiii!!!!
    rez = dict(reduce(lambda acc,el: acc | {str(el[0]): el[1:] if el[1:] else None}, A, dict()))
    print(rez)

operacija([(1, 4, 6), (2, 4), (4, 1)], lambda x, y: x + y)
objedini([(1), (3, 4, 5), (7), (1, 4, 5), (6, 2, 1, 3)])