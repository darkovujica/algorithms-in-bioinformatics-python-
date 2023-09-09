k = int(input())
d = int(input())
f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba2a (1).txt", "r")
patterns = f.read().splitlines()[1:]


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

lista=[]
lista2=[]
for i in range(len(patterns[0])-k+1):
    lista2.extend(Neighbors(patterns[0][i:i+k],d))

for el in lista2:
    if el not in lista:
        lista.append(el)

for j in range(1,len(patterns)):
    lis = []
    for i in range(len(patterns[j])-k+1):
        lis.extend(Neighbors(patterns[j][i:i+k],d))  # moglo je i pomoću
    lista = [el for el in lista if el in lis]        # Count iz BA1I zad
    
for l in lista:
    print(l, end=" ")
