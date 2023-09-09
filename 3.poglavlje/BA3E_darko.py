f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba3e (1).txt", "r")
patterns = f.read().splitlines()

k = len(patterns[0]) - 1  #!!!!

lista = {}
for i in patterns:
    if i[:-1] not in lista:
        lista[i[:-1]] = [i[1:]]
    else:
        lista[i[:-1]].append(i[1:])
        
fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba3ee.txt", 'w')

for el in lista.keys():
    string = ""
    for p in lista[el]:
        string = string + p + ","
    if string != "":
        fp.write(el + " -> " + string[:-1] + "\n")
fp.close()
