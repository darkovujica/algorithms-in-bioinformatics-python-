f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba2h.txt", "r")
patterns = f.read().splitlines()
pat = patterns[0]
patterns = patterns[1].split()


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

br = 0
for text in patterns:
    br = br + MinHam(text, pat)
    
print(br)
