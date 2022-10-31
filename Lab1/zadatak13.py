from itertools import pairwise


def izmeni(lista):
    rez = [lista[i] + 1 if i %2 == 0 else lista[i] - 1 for i in range(len(lista))]
    print(rez)

def produzi(lista,br):
    n = br - len(lista)
    pom = n*[0]
    lista.extend(pom)
    return lista

def skupi(lista):
    maxLen = max(len(x) for x in lista)
    pom = [produzi(x,maxLen) if len(x) < maxLen else x for x in lista]
    pom = list(pairwise(pom))
    rez = [list(map(lambda x,y: x + y, pom[i][0],pom[i][1]))for i in range(len(pom))]
    print(rez)

skupi([[1, 3, 5],[2, 4, 6],[1, 2]])
izmeni([8, 5, 3, 1, 1])    