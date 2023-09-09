text = input()

def Reverse(text):
    s = ""
    for i in text:
        if i == "A":
            s = "T" + s
        elif i == "T":
            s = "A" + s
        elif i == "C":
            s = "G" + s
        elif i == "G":
            s = "C" + s
    return s

print(Reverse(text))
