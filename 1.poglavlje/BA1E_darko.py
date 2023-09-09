fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba1e (2).txt", 'r')
unos = fp.read().splitlines()
text = unos[0]
k = int(unos[1].split()[0])
L = int(unos[1].split()[1])
t = int(unos[1].split()[2])

def Count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count = count + 1
    return count

def FrequencyList(text, k, t):
    l = []
    for i in range(len(text) - k + 1):
        rijec = text[i : i + k]
        q = Count(text[i:], rijec)
        if(q >= t and rijec not in l):
            l.append(rijec)
    return l

lista = [] ##lista da bismo izbjegli ponavljanje ispisa

for i in range(len(text) - L):
    l = FrequencyList(text[i:i+L], k, t)
    for j in l:
        if j not in lista:
            lista.append(j)

f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba1ee.txt", 'w')
for i in lista:
    f.write(i + " ")
f.close()
