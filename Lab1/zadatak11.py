from functools import reduce
from itertools import pairwise


def razlika(lista):
    tapl = list(pairwise(lista))
    rez = [tapl[i][0] - tapl[i][1] for i in range(len(tapl))]
    print(rez)

def proizvod(lista):
    rez = [lista[i] if type[lista[i]] in (int,float) else reduce(lambda x,y: x*y, lista[i]) for i in range(len(lista))]
    print(reduce(lambda x,y: x*y,rez))

razlika([8, 5, 3, 1, 1])
proizvod([[1, 3, 5],[2, 4, 6],[1, 2, 3]])