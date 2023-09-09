f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba3e.txt", "r")
patterns = f.read().splitlines()

def Graph(edges):
    D = {}
    for edge in edges:
        first, second = edge.split(" -> ")
        second = second.split(",")
        D[first] = second
    return D

g = Graph(patterns)
node = list(g.keys())[0]
lista = [node]              # u nju čvorove slažemo kako putujemo

while len(g.keys()) > 0:
    el = g[node][0]
    lista.append(el)

    g[node].pop(0)
    if len(g[node]) == 0:
        del(g[node])

    node = el
    if node not in list(g.keys()):
        for i in range(len(lista)):
            if lista[i] in g.keys():
                node = lista[i]
                lista = lista[i:] + lista[1:i+1]
                break

string=""
for i in lista:
    string = string + i + "->"

fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba3ff.txt", 'w')
fp.write(string[:-2])
fp.close()
            
