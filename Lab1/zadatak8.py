from functools import reduce
import operator


def zameni(lista):
   rez = [reduce(operator.add,lista[:i+1]) if len(lista[:i+1]) > 1 else lista[i] for i in range(len(lista))]
   print(rez)


def izracunaj(lista):
    rez = [lista[i] if type(lista[i]) != list else reduce(lambda x,y: x*y, lista[i]) for i in range(len(lista))]
    print(rez)

lista = [1, 2, 4, 7, 9]
zameni(lista) 
izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]])