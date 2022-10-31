from functools import reduce
from itertools import filterfalse


def presek(l1,l2):
    rez = list(filterfalse(lambda x: x not in l2,l1))
    print(rez)
    rez2 = list(filterfalse(lambda x: x not in l1,l2))
    print(rez2)
    
def izracunaj(lista):
    rez = [x**2 if type(x) in (int,float) else reduce(lambda x,y: x**2 + y**2, x) for x in lista]
    print(rez)

presek([5, 4, "1", "8", 3, 7], [1, 9, "1"])
izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]) 