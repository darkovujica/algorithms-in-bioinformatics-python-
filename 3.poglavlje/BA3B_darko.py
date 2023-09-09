f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba3b.txt", "r")
patterns = f.read().splitlines()

s = patterns[0][:-1]
for string in patterns:
    s = s + string[-1]
print(s)
