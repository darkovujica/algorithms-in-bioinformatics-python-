fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba5d.txt", 'r')
unos = fp.read().splitlines()
i = unos[0]
j = unos[1]
edges = unos[2:]

def Graph(edges):
    D = {}
    for edge in edges:
        first, second = edge.split("->")
        second, weight = second.split(":")
        if first not in D.keys():
            D[first] = []
        D[first].append([second,int(weight)])
    return D

def Paths(graf, i, j, path, L):
    if i==j:
        L.append(path)
        return
    if i not in graf.keys():
        return

    for node in graf[i]:
        Path = path.copy()
        Path.append([i,node[0],node[1]])
        Paths(graf,node[0],j,Path,L)
        
    return L

def LongestPath(L):
    ss = -1
    putt = ""
    for i in range(len(L)):
        put = L[i]
        s = 0
        for edge in put:
            s += edge[2]
        if s>ss or ss==-1:
            ss = s
            putt = put
    print(s)
    
    string = ""
    for edge in putt:
        string += edge[0] + "->"
        
    string += j
    print(string)
            

graf = Graph(edges)
L = Paths(graf,i,j,[],[])
LongestPath(L)

    
