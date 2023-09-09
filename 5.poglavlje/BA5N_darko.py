def TopologicalOrdering(Graph):
    List = []
    Outgoing = []
    for v in Graph.values():
        Outgoing=Outgoing+v
    Outgoing=set(Outgoing)
    Candidates=[]
    for k in Graph.keys():
        if k not in Outgoing:
            Candidates.append(k)
    while len(Candidates)>0:
        a=Candidates[0]
        List.append(a)
        Candidates.remove(a)
        if a in Graph.keys():
            d=len(Graph[a])
            for i in range (d):
                b=Graph[a][0]
                Graph[a].pop(0)
                Outgoing=[]
                for v in Graph.values():
                    Outgoing = Outgoing + v
                Outgoing = set(Outgoing)
                if b not in Outgoing:
                    Candidates.append(b)

    for k in Graph.keys():
        if len(Graph[k])>0:
            return "the input graph is not a DAG"
    return ", ".join(List)


f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba5n.txt", "r")
inlines = f.read().splitlines()

graph = dict()
for i in inlines:
    pair = i.split(" -> ")
    graph[pair[0]] = pair[1].split(",")
res = TopologicalOrdering(graph)
print(res)


