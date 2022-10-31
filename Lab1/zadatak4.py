def zbir(lista):
    rez = [lista[i] + lista[i+1] for i in range(len(lista)-1)]
    print(rez)
    
def suma(lista):
    rez = [lista[i][j] for i in range(len(lista)) for j in range(len(lista[i]))]
    broj = sum(rez)
    print(rez)
    print(broj)


lista = [1,2,3,4,5]
zbir(lista)
suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]])