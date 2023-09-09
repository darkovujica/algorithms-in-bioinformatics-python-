fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba4b (1).txt", 'r')
pat = fp.read().splitlines()
dna = pat[0]
peptide = pat[1]
k = len(peptide)

gencode = {
        "AAA": "K","AAC": "N","AAG": "K","AAU": "N","ACA": "T","ACC": "T",
        "ACG": "T","ACU": "T","AGA": "R","AGC": "S","AGG": "R","AGU": "S",
        "AUA": "I","AUC": "I","AUG": "M","AUU": "I","CAA": "Q","CAC": "H",
        "CAG": "Q","CAU": "H","CCA": "P","CCC": "P","CCG": "P","CCU": "P",
        "CGA": "R","CGC": "R","CGG": "R","CGU": "R","CUA": "L","CUC": "L",
        "CUG": "L","CUU": "L","GAA": "E","GAC": "D","GAG": "E","GAU": "D",
        "GCA": "A","GCC": "A","GCG": "A","GCU": "A","GGA": "G","GGC": "G",
        "GGG": "G","GGU": "G","GUA": "V","GUC": "V","GUG": "V","GUU": "V",
        "UAA": "*","UAC": "Y","UAG": "*","UAU": "Y","UCA": "S","UCC": "S",
        "UCG": "S","UCU": "S","UGA": "*","UGC": "C","UGG": "W","UGU": "C",
        "UUA": "L","UUC": "F","UUG": "L","UUU": "F"}

def ToAmino(rna):
    string = ""
    for i in range(0,len(rna),3):
        s = gencode[rna[i:i+3]]
        if s=="*":
            break
        string = string + s
    return string

def DNAtoRNA(dna):
    s = ""
    for i in dna:
        if i == "T":
            s = s + "U"
        else:
            s = s + i
    return s

def Reverse(dna):
    s = ""
    for i in dna:
        if i == "A":
            s = "T" + s
        elif i == "T":
            s = "A" + s
        elif i == "C":
            s = "G" + s
        elif i == "G":
            s = "C" + s
    return s

rna = DNAtoRNA(dna)
rna2=DNAtoRNA(Reverse(dna))
print(dna)
print(Reverse(dna))
print(rna)
print(rna2)
f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba4bb.txt", 'w')

for i in range(len(rna)-3*k+1):
    if(ToAmino(rna[i:i+3*k])==peptide or ToAmino(rna2[i:i+3*k])==peptide):
        f.write(dna[i:i+3*k] + "\n")
f.close()
