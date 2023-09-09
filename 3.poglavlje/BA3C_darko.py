f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba3c.txt", "r")
patterns = f.read().splitlines()

patterns.sort()
k = len(patterns[0])

fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba3c.txt", "w")

for pat in patterns:
    for p in patterns:
        if pat[1:] == p[:k-1]:
            fp.write(pat + " -> " + p + "\n")

fp.close()
