k = int(input())
text = input()

k = k-1 #!!!!!!

lista = []
for i in range(len(text)-k+1):
    if text[i:i+k] not in lista:
        lista.append(text[i:i+k])
        
lista.sort()
fp = open("C:\\Users\\DARKO\\Downloads\\ba3dd.txt", 'w')
for l in lista:
    string = ""
    for p in lista:
        if l[1:] == p[:k-1]:
            string = string + p + ","
    if string != "":
        fp.write(l + " -> " + string[:-1] + "\n")
fp.close()
