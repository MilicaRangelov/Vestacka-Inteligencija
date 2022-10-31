def razlika(l1, l2):
    print([x for x in l1 if x not in l2])

def objedini(l1,l2):
    kraca = l1 if len(l1) <= len(l2) else l2
    duza = l1 if len(l1) > len(l2) else l2
    pom = [0]*(len(duza) - len(kraca))
    kraca.extend(pom)
    print([(duza[i], kraca[i]) if duza[i] < kraca[i] else (kraca[i], duza[i]) for i in range(len(kraca))])


lista1 =[1,4,6,'6',5]
lista2 = [4,6,'6']
razlika(lista1, lista2) 
lista1 =[1, 7, 2, 4, 5]
lista2 = [2, 5, 2]
objedini(lista1, lista2)