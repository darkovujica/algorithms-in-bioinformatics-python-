f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba3h.txt", "r")
patterns = f.read().splitlines()

k = int(patterns[0])  #!!!!     ovo je iz E zadatka
patterns = patterns[1:]

g = {}
for i in patterns:
    if i[:-1] not in g.keys():
        g[i[:-1]] = [i[1:]]
    else:
        g[i[:-1]].append(i[1:])   
        

def Start(g):                       # dalje je iz G zadatka
    for i in g.keys():
        br = len(g[i])
        for j in g.values():
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
                poc = node
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
    return lista


lista = Poredak(g)

s = lista[0][:-1]             # ovo je iz B zadatka
for string in lista:
    s = s + string[-1]

fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba3hh.txt", 'w')
fp.write(s)
fp.close()
