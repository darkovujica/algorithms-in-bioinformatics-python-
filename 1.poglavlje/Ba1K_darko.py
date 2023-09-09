text = input()
k = int(input())

def SymbolToNumber(s):
    if s=="A":
        return 0
    elif s=="C":
        return 1
    elif s=="G":
        return 2
    else:
        return 3
    
def PatternToNumber(patt):
    if patt == "":
        return 0
    return 4*PatternToNumber(patt[:-1]) + SymbolToNumber(patt[-1:-2:-1])

l = [0 for i in range(4**k)]

for i in range(len(text)-k+1):
    l[PatternToNumber(text[i:i+k])] +=1

for i in l:
    print(i, end=" ")
