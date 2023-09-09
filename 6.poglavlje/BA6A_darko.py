def greedySorting(P):
    approxReversalDistance=0
    reversalList=[]
    for k in range (1,len(P)+1):
        newP=[]
        if (P[k-1]!=k):
            l=0
            if (k in P):
                l=P.index(k)
            if (-k in P):
                l=P.index(-k)
            newP = P.copy()
            for i in range (k-1,l+1):
                newP[i]=-P[l-(i-k)-1]
            reversalList.append(newP)
            P=newP
            approxReversalDistance=approxReversalDistance+1
        if (P[k-1]==-k):
            newP=P.copy()
            newP[k-1]=k
            reversalList.append(newP)
            P=newP
            approxReversalDistance=approxReversalDistance+1
    return reversalList


x = "(+24 -91 +19 +8 -112 +13 +5 -60 -89 +53 -118 -130 -131 +17 +88 -71 -121 -2 +47 -110 +123 -54 -70 +16 -20 +69 +59 +41 +100 -108 -46 -40 -107 +49 -103 -75 -76 -74 +34 +37 +119 +73 -96 +86 +84 -87 -61 -93 +39 +15 +128 +90 -45 -106 -43 -23 +127 -117 -50 +30 -81 +63 +52 +57 -92 +25 +120 +68 -28 -97 -116 -95 +33 -83 -51 -98 +115 +79 +109 -72 +12 -129 +122 +29 +101 -18 +35 +80 +125 -111 +9 +6 +82 +102 +78 +114 +42 +10 +113 -62 +4 -14 +31 -104 +55 -36 +26 +124 -85 -99 +7 +77 -27 +126 +11 -22 +38 +64 -56 -94 -44 -67 +32 -1 +21 -3 -66 +65 +48 +105 -58)"

P = x.split(" ")
P[0] = P[0][1:]
P[len(P) - 1] = P[len(P) - 1][:-1]
for i in range(len(P)):
    P[i] = int(P[i])
res = greedySorting(P)
pr = []
for L in res:
    for i in range(len(L)):
        if L[i] > 0:
            L[i] = "+" + str(L[i])
        else:
            L[i] = str(L[i])
    pr.append(("(" + " ".join(L) + ")"))
resfin = "\n".join(pr)
print(resfin)
