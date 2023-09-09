f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba3g.txt", "r")
patterns = f.read().splitlines()

def Graph(edges):
    D = {}
    for edge in edges:
        first, second = edge.split(" -> ")
        second = second.split(",")
        D[first] = second
    return D

def Start(g):
    for i in g.keys():
        br = len(g[i])        # u koga taj element vodi
        for j in g.values():  # minus oni koji vode u njega
            if i in j:
                br = br - 1
        if br == 1:
            return i
        
def Poredak(g):
    
    poc = Start(g)
    node = poc
    lista = [node]
    da = False
    
    while len(g.keys()) > 0:
        el = g[node][0]
        lista.append(el)

        g[node].pop(0)
        if len(g[node]) == 0:
            del(g[node])

        node = el
        if node not in list(g.keys()):
            if node != lista[0]:
                g[node] = [poc]
                da = True
                poc = node         # nije pocetak, nego uljez!!!
                continue
            for i in range(len(lista)):
                if lista[i] in g.keys():
                    node = lista[i]
                    lista = lista[i:] + lista[1:i+1]
                    break
    if da==True:
        for i in range(len(lista)):
            if lista[i] == poc:
                lista = lista[i+1:] + lista[1:i+1]
                break


g = Graph(patterns)
lista = Poredak(g)

string=""
for i in lista:
    string = string + i + "->"

fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba3gg.txt", 'w')
fp.write(string[:-2])
fp.close()
            
