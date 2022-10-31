from functools import reduce
import operator

def brojel(lista):
    print([len(x) if type(x) == list else -1 for x in lista])

def proizvod(lista1, lista2):
    rez = [reduce(operator.add, lista1[i]) * lista2[i] for i in range(len(lista1))]
    print(rez)    

brojel([[1,2,3],"heh", [1,2]])
proizvod([[1,2,3],[4,5,6],[7,8,9]], [1,2,3]) 