k = int(input())
t = int(input())
fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba2d.txt", 'r')
RowList = fp.read().splitlines()[1:]

def Profile(matrica):
    d = {"A":[0]*k,"C":[0]*k,"G":[0]*k,"T":[0]*k}
    for rijec in matrica:
        for i in range(k):
            d[rijec[i]][i] += 1/len(matrica)
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
        
    

BestMotifs = [x[:k] for x in RowList]
first_row = RowList[0]

for i in range(len(first_row)-k+1):
    #dic = {}
    #dic["motif1"] = first_row[i:i+k]
    motifs = [first_row[i:i+k]]
    for j in range(1,t):
        #motifs = [dic["motifs"+str(k)] for k in range(1,i)]
        pro = Profile(motifs)
        motifs.append(Czadatak(pro,RowList[j]))
        #dic["motif"+str(j)] =
    if Score(motifs) < Score(BestMotifs):
        BestMotifs = motifs

for i in BestMotifs:
    print(i)

        
