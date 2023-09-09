fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba1h (1).txt", 'r')
unos = fp.read().splitlines()
print(unos)
fp.close()

DNA = unos[0]
Text = unos[1]
HammingMax = int(unos[2])

def Hamming(DNA1, DNA2):
    counter = 0
    for i in range(len(DNA1)):
        if(DNA1[i] != DNA2[i]):
            counter += 1
    return counter

f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba1hh.txt", 'w')
for i in range(len(Text) - len(DNA) + 1):
    if(Hamming(Text[i:i+len(DNA)],DNA)<=HammingMax):
        f.write(str(i) + " ")  
f.close()
