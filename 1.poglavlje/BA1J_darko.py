text=input()
k=int(input())
d=int(input())

tekst = ""
for i in text:
    if i=="A":
        tekst = "T" + tekst
    elif i=="T":
        tekst = "A" + tekst
    elif i=="G":
        tekst = "C" + tekst
    else:
        tekst = "G" + tekst
# tekst je reverse complement

def Hamming(DNA1, DNA2):
    counter = 0
    for i in range(len(DNA1)):
        if(DNA1[i] != DNA2[i]):
            counter += 1
    return counter
    
def Count(DNA):
    br = 0
    a = []
    for i in range(len(text) - len(DNA)):
        if(Hamming(text[i:i+len(DNA)],DNA)<= d):
            br=br+1
        if(Hamming(tekst[i:i+len(DNA)],DNA)<= d):
            br=br+1
    return br

# radimo sve moguće kombinacije
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

s = [Count(rij) for rij in l]
m = max(s)
for i in range(4**k):
    if s[i] == m:
        print(l[i])
