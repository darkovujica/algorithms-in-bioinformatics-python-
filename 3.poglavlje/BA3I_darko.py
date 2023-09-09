k = int(input())

l=[]
for i in range(2**k):
    rijec=""
    for j in range(k):
        ost = i%2
        i = i//2
        if ost==0:
            rijec = "0" + rijec
        else:
            rijec = "1" + rijec
    l.append(rijec)

g = {}
for i in l:
    if i[:-1] not in g.keys():
        g[i[:-1]] = [i[1:]]
    else:
        g[i[:-1]].append(i[1:])


def Poredak(g):
    node = list(g.keys())[0]
    lista = [node]
    
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
    return lista


lista = Poredak(g)

s = lista[0][:-1]
for string in lista:
    s = s + string[-1]

print(s[:-k+1])   # jer je krug, a ne niz...
