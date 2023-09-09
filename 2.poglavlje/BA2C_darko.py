text = input()
k = int(input())
f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba2c.txt", "r")
patterns = f.read().splitlines()[2:]


rij={}
niz = ["A","C","G","T"]
vj = []

for i in range(len(patterns)):
    rij[niz[i]]=patterns[i].split()

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
        print(text[i:i+k])
        break
