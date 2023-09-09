i = int(input())
k = int(input())

l=[]
rijec=""
for j in range(k):
    ost = i%4
    i = i//4
    if ost==0:
        rijec = "A" + rijec
    elif ost==1:
        rijec = "C" + rijec
    elif ost==2:
        rijec = "G" + rijec
    else:
        rijec = "T" + rijec
print(rijec)
