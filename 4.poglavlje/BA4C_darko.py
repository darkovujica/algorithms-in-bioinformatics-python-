fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba4c.txt", 'r')
peptide = fp.read().splitlines()[0]

amino = {
        'G': 57,
        'A': 71,
        'S': 87,
        'P': 97,
        'V': 99,
        'T': 101,
        'C': 103,
        'I': 113,
        'L': 113,
        'N': 114,
        'D': 115,
        'K': 128,
        'Q': 128,
        'E': 129,
        'M': 131,
        'H': 137,
        'F': 147,
        'R': 156,
        'Y': 163,
        'W': 186}

def Masa(pep):
    br = 0
    for i in pep:
        br = br + amino[i]
    return br

def Cyclo(peptide):
    lista = [0,Masa(peptide)]
    k = len(peptide)
    peptide += peptide

    for i in range(1,k):
        for j in range(k):
            lista.append(Masa(peptide[j:j+i]))
    return sorted(lista)
        

f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba4cc.txt", 'w')
for el in Cyclo(peptide):
    f.write(str(el) + " ")
f.close()
