pattern = input()

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

print(PatternToNumber(pattern))
