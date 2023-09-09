k = int(input())
f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba2b.txt", "r")
patterns = f.read().splitlines()[1:]


niz = ["A","C","G","T"]

def Hamming(DNA1, DNA2):
    counter = 0
    for i in range(len(DNA1)):
        if(DNA1[i] != DNA2[i]):
            counter += 1
    return counter

def MinHam(text, pattern):
    h = -1
    for i in range(len(text) - len(pattern) + 1):
        hh = Hamming(text[i:i+len(pattern)],pattern)
        if hh<h or h==-1:
            h=hh
    return h


l=[]
for i in range(4**k):
    rijec=""
    for j in range(k):
        ost = i%4
        i = i//4
        if ost==0:
            rijec = "A" + rijec
        elif ost==1:
            rijec = "T" + rijec
        elif ost==2:
            rijec = "G" + rijec
        else:
            rijec = "C" + rijec
    l.append(rijec)

d = -1
for pat in l:
    br = 0
    for text in patterns:
        br = br + MinHam(text, pat)
    if br<d or d==-1:
        d = br
        median = pat

print(median)
