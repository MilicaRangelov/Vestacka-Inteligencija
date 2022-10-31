from functools import reduce
from itertools import pairwise


def izbroj(lista):
    return reduce(lambda x,y: x + (1 if type(y) in (int,float) else izbroj(y)), lista,0)

def stepen(lista):
    tapl = list(pairwise(lista))
    rez = [tapl[i][0]** tapl[i][1] for i in range(len(tapl))]
    print (rez)    

stepen([1, 5, 2, 6, 1, 6, 3, 2, 9])