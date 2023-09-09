f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba3l.txt", "r")
patterns = f.read().splitlines()
k = int(patterns[0].split()[0])
d = int(patterns[0].split()[1])
patterns = patterns[1:]

st = patterns[0][:k]
for p in patterns:
    if(p != patterns[0]):
        st += p[k - 1]
#sada smo nalijepili sve iz prvog člana para, sada moramo one iz drugog pri kraju

for i in range(k + d):
    st += patterns[len(patterns) - (k + d) + i][-1]

fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba3ll.txt", 'w')
fp.write(st)
fp.close()
