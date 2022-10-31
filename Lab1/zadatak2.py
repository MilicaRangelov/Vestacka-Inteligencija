def numlist(lista):
    rezultat = []
    for i in range(len(lista)):

        if(type(lista[i]) in [int, float]):
            rezultat.append(lista[i])
    
    print(f"Nakon izmene {rezultat}")      

def spojidict(lista1, lista2):
    kraca = lista1 if len(lista1) <= len(lista2) else lista2
    duza = lista1 if len(lista1) > len(lista2) else lista2
    print(f"Kraca {kraca}, Duza {duza}")
    n = len(duza) - len(kraca)
    pom = n*['-']
    kraca.extend(pom)

    rez = list(map(lambda x,y: {"prvi" : x, "drugi" : y}, kraca,duza))
    print(rez)
    

lista = ["Prvi","Drugi",2,4,[5,6]]
numlist(lista)
spojidict([1, 7, 2, 4], [2, 5, 2])