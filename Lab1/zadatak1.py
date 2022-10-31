
def parni(lista):
    broj = 0
    for b in lista:
        if b %2 == 0:
            broj+=1

    print(f"Lista: {lista}, broj panrnih brojeva {broj}")


def poredak(lista1, lista2):
    kraca = lista1 if len(lista1) <= len(lista2) else lista2
    duza = lista1 if len(lista1) > len(lista2) else lista2
    print(f"Kraca {kraca}, Duza {duza}")
    n = len(duza) - len(kraca)
    pom = n*[0]
    kraca.extend(pom)

    rezultat = list(map(lambda x,y: (x,y,"Jeste") if 2*x < y else (x,y,"Nije"), kraca,duza))
    print(rezultat)
  
lista1 = [1,7,2,4]
lista2 = [2,5,2,5]

poredak(lista1,lista2)