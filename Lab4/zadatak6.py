
import copy

rezultat = dict()
graph = {
'1' : set([1,2,3,4,5,6,7,8]),  
'2' : set([1,2,3,4,5,6,7,8]),
'3' : set([1,2,3,4,5,6,7,8]),
'4' : set([1,2,3,4,5,6,7,8]),
'5' : set([1,2,3,4,5,6,7,8]),
'6' : set([1,2,3,4,5,6,7,8]),
'7' : set([1,2,3,4,5,6,7,8]),
'8' : set([1,2,3,4,5,6,7,8])
}



def mvr(dostupne):
    minKey = list(dostupne.keys())[0]
    min = len(dostupne[minKey])

    for key, values in dostupne.items():
        if len(values) < min:
            min = len(values)
            minKey = key
    
    return minKey       

def indeksiDijagonala(koordinate):
  
    indeksi = set()
    for dI in range(1,9):
        #gore desno
        if koordinate[0] - dI >= 1 and koordinate[0]- dI <= 8 and koordinate[1]+dI >= 1 and koordinate[1]+dI <=8:
            indeksi.add(tuple([koordinate[0]-dI,koordinate[1]+dI]))
        #gore levo
        if koordinate[0] - dI >= 1 and koordinate[0]-dI <=8 and koordinate[1]-dI >= 1 and koordinate[1]-dI <=8:
            indeksi.add(tuple([koordinate[0] - dI,koordinate[1]-dI]))  
        #dole desno
        if koordinate[0] + dI >= 1 and koordinate[0]+dI <=8 and koordinate[1]+dI >= 1 and koordinate[1]+dI <=8:
            indeksi.add(tuple([koordinate[0] + dI,koordinate[1]+dI])) 
        #dole levo
        if koordinate[0] + dI >= 1 and koordinate[0]+dI <=8 and koordinate[1]-dI >= 1 and koordinate[1]-dI <=8:
            indeksi.add(tuple([koordinate[0] + dI,koordinate[1]-dI]))         
        

    return indeksi          

    
    

def noviDomeni(graph,koordinateKraljice):

    dijagonale = indeksiDijagonala(koordinateKraljice)
    noviGraph = dict()

    for kljuc in graph.keys():
        noviGraph.update({kljuc : copy.deepcopy(graph[kljuc]) })

        if int(kljuc) == koordinateKraljice[0]:
            noviGraph.pop(kljuc)
            continue
        
        if koordinateKraljice[1] in noviGraph[kljuc]:
            noviGraph[kljuc].remove(koordinateKraljice[1])

        vrsta = int(kljuc)
        for kor in dijagonale:
            if kor[0] == vrsta and kor[1] in noviGraph[kljuc]:
                noviGraph[kljuc].remove(kor[1])
                if len(noviGraph[kljuc]) == 0:
                    return None,True

    failed = False

    # for kljuc in noviGraph.keys():
    #     if len(noviGraph[kljuc]) == 0:
    #         failed = True
    #         break

    return noviGraph,failed    
    

            


def forward_checking(graph):

    if len(graph) == 0:
        return True

    variable = mvr(graph)
    noviGraph = {}
    failed = False

    for possible_value in graph[variable]:
        koordinateKraljice = (int(variable),possible_value)  
        noviGraph, failed = noviDomeni(graph, koordinateKraljice) 
        
        if failed == True:
            continue
        else:
            rezultat[variable] = koordinateKraljice[1]
            if forward_checking(noviGraph) != False:
                    return True

    return False    

def printChessBoard(promenljive):
        tabla = ""
        i=1
        for kljuc in sorted(promenljive.keys()):
            v,k = int(kljuc),promenljive[kljuc]
            for j in range (1,9):
                tabla += "Q " if v==i and j ==k else "_ "

            tabla += '\n'    
            i+=1
        print(tabla)  


if forward_checking(graph) == True:
    print(rezultat)
    printChessBoard(rezultat)