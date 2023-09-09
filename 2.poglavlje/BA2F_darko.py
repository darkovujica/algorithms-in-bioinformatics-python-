import random,time

k = int(input())
t = int(input())
fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba2f.txt", 'r')
RowList = fp.read().splitlines()[1:]

def Profile(matrica):
    r = 4+ len(matrica)
    d = {"A":[r]*k,"C":[r]*k,"G":[r]*k,"T":[r]*k}  # prije bilo 0
    for rijec in matrica:
        for i in range(k):
            d[rijec[i]][i] += 1/r        # prije bilo len(matrica)
    return d

def Czadatak(rij,text):
    vj = []

    for i in range(len(text)-k+1):
        vjer = 1
        br = 0
        for slovo in text[i:i+k]:
            vjer = float(rij[slovo][br]) * vjer
            br = br+1
        vj.append(vjer)

    m = max(vj)
    for i in range(len(vj)):
        if vj[i]==m:
            return text[i:i+k]

def Score(motifs):
    br = 0
    d =  {"A":0,"C":1,"G":2,"T":3}
    for j in range(len(motifs[0])):
        l = [0,0,0,0]
        for m in motifs:
            l[d[m[j]]] += 1
        br += len(motifs) - max(l)
    return br

def randomMotifs(RowList):
    r_motifs = []
    for i in range(len(RowList)):
        random.seed(i + time.time())
        r = random.randint(0, len(RowList[0]) - k)
        r_motifs.append(RowList[i][r : r + k])
    return r_motifs
    

Motifs = randomMotifs(RowList)
BestMotifs = Motifs

for i in range(1000):
    Motifs = randomMotifs(RowList)
    
    while(True):
        pro = Profile(Motifs)
        Motifs = []
        for j in range(t):
            Motifs.append(Czadatak(pro,RowList[j]))

        if(Score(Motifs) < Score(BestMotifs)):
            BestMotifs = Motifs
        else:
            break

for i in BestMotifs:
    print(i)
print(Score(BestMotifs))
        
