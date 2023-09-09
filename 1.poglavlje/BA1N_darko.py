pattern = input()
d = int(input())

niz = ["A","C","G","T"]

def Hamming(DNA1, DNA2):
    counter = 0
    for i in range(len(DNA1)):
        if(DNA1[i] != DNA2[i]):
            counter += 1
    return counter

def Neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern)==1:
        return ["A","C","G","T"]
    
    neig = []
    sufneig = Neighbors(pattern[1:],d)
    
    for rij in sufneig:
        if Hamming(rij, pattern[1:])<d:
            for i in niz:
                neig.append(i + rij)
        else:
            neig.append(pattern[0] + rij)
    return neig

lista = Neighbors(pattern,d)
for l in lista:
    print(l)
