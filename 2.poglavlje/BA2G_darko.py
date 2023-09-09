import random,time

fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba2g (3).txt", 'r')
RowList = fp.read().splitlines()
k = int(RowList[0].split()[0])
t = int(RowList[0].split()[1])
N = int(RowList[0].split()[2])
RowList = RowList[1:]
fp.close()

def Profile(matrica):
    r = 4+ len(matrica)
    d = {"A":[r]*k,"C":[r]*k,"G":[r]*k,"T":[r]*k}  # prije bilo 0
    for rijec in matrica:
        for i in range(k):
            d[rijec[i]][i] += 1/r        # prije bilo len(matrica)
    return d

def Czadatak(rij,text):
    vj = []
    rijeci = []

    for i in range(len(text)-k+1):
        vjer = 1
        br = 0
        rijeci.append(text[i:i+k])
        
        for slovo in text[i:i+k]:
            vjer = float(rij[slovo][br]) * vjer
            br = br+1
        vj.append(vjer)

    random.seed(time.time())
    Rmotif = random.choices(rijeci, vj)[0]
    return Rmotif

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

def GibbsSampler(RowList, k, t, N):
    Motifs = randomMotifs(RowList)
    bestmotifs = Motifs
    for i in range(N):
        n = random.randint(0, t - 1)
        tmp = Motifs.copy()
        tmp.pop(n)
        prof = Profile(tmp)
        Motifs[n] = Czadatak(prof,RowList[n])
        if(Score(Motifs) < Score(bestmotifs)):
            bestmotifs = Motifs
    return bestmotifs
    
    

Motifs = GibbsSampler(RowList, k, t, N)
BestMotifs = Motifs

for i in range(19):
    Motifs = GibbsSampler(RowList, k, t, N)
    if Score(Motifs) < Score(BestMotifs):
        BestMotifs = Motifs

for i in BestMotifs:
    print(i)
print(Score(BestMotifs))
        
