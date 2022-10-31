
def uredi(lista, n, vrednost):
    lista[:n] =list(map(lambda x: x+vrednost , lista[:n]))
    lista[n:] =list(map(lambda x: x-vrednost , lista[n:]))
    print(lista)

def spoj(lista1, lista2):
    kraca = lista1 if len(lista1) <= len(lista2) else lista2
    duza = lista1 if len(lista1) > len(lista2) else lista2
    print(f"Kraca {kraca}, Duza {duza}")
    n = len(duza) - len(kraca)
    pom = n*[0]
    kraca.extend(pom)
    print(f"Nakon izmene {kraca}")
    rez = list(map( lambda x,y: (x[1] ,y, x[1]+y) if (x[1] < y and x[0] < len(kraca) - 1) else (y,x[1],x[1]+y) , list(enumerate(kraca)), duza))
    print(rez)

uredi([1,2,3,4,5],3,1)    
spoj([1,7,2,4], [2,5,2])