fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba1g.txt", 'r')
unos = fp.read().splitlines()
a = unos[0]
b = unos[1]
fp.close()

def Index():
    index={
        "A":0,"C":1,"D":2,"E":3,"F":4,"G":5,"H":6,"I":7,"K":8,"L":9,"M":10,
        "N":11,"P":12,"Q":13,"R":14,"S":15,"T":16,"V":17,"W":18,"Y":19}
    return index

def Penality():
    penality={
        "A":[4,  0, -2, -1, -2,  0, -2, -1, -1, -1, -1, -2, -1, -1, -1,  1,  0,  0, -3, -2],
        "C":[0,  9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
        "D":[-2, -3,  6,  2, -3, -1, -1, -3, -1, -4, -3,  1, -1,  0, -2,  0, -1, -3, -4, -3],
        "E":[-1, -4,  2,  5, -3, -2,  0, -3,  1, -3, -2,  0, -1,  2,  0,  0, -1, -2, -3, -2],
        "F":[-2, -2, -3, -3,  6, -3, -1,  0, -3,  0,  0, -3, -4, -3, -3, -2, -2, -1,  1,  3],
        "G":[0, -3, -1, -2, -3,  6, -2, -4, -2, -4, -3,  0, -2, -2, -2,  0, -2, -3, -2, -3],
        "H":[-2, -3, -1,  0, -1, -2,  8, -3, -1, -3, -2,  1, -2,  0,  0, -1, -2, -3, -2,  2],
        "I":[-1, -1, -3, -3,  0, -4, -3,  4, -3,  2,  1, -3, -3, -3, -3, -2, -1,  3, -3, -1],
        "K":[-1, -3, -1,  1, -3, -2, -1, -3,  5, -2, -1,  0, -1,  1,  2,  0, -1, -2, -3, -2],
        "L":[-1, -1, -4, -3,  0, -4, -3,  2, -2,  4,  2, -3, -3, -2, -2, -2, -1,  1, -2, -1],
        "M":[-1, -1, -3, -2,  0, -3, -2,  1, -1,  2,  5, -2, -2,  0, -1, -1, -1,  1, -1, -1],
        "N":[-2, -3,  1,  0, -3,  0,  1, -3,  0, -3, -2,  6, -2,  0,  0,  1,  0, -3, -4, -2],
        "P":[-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2,  7, -1, -2, -1, -1, -2, -4, -3],
        "Q":[-1, -3,  0,  2, -3, -2,  0, -3,  1, -2,  0,  0, -1,  5,  1,  0, -1, -2, -2, -1],
        "R":[-1, -3, -2,  0, -3, -2,  0, -3,  2, -2, -1,  0, -2,  1,  5, -1, -1, -3, -3, -2],
        "S":[1, -1,  0,  0, -2,  0, -1, -2,  0, -2, -1,  1, -1,  0, -1,  4,  1, -2, -3, -2],
        "T":[0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1,  0, -1, -1, -1,  1,  5,  0, -2, -2],
        "V":[0, -1, -3, -2, -1, -3, -3,  3, -2,  1,  1, -3, -2, -2, -3, -2,  0,  4, -3, -1],
        "W":[-3, -2, -4, -3,  1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11,  2],
        "Y":[-2, -2, -3, -2,  3, -3,  2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1,  2,  7]
        }
    return penality


def Manh(a,b):                     # iz C zadatka
    n = len(a)
    m= len(b)
    
    penality = Penality()
    index = Index()
    s = []
    back = []
    
    for i in range(n+1):
        s.append((m+1)*[0])
        back.append((m+1)*[0])

    for i in range(n+1):
        s[i][0] = -5*i
    for i in range(m+1):
        s[0][i] = -5*i
        
    for i in range(1,n+1):
        for j in range(1,m+1):
            x = penality[a[i-1]][index[b[j-1]]]
            s[i][j] = max(s[i][j-1]-5,s[i-1][j]-5,s[i-1][j-1] + x) 

            if s[i][j] == s[i-1][j]-5:
                back[i][j] = "d"
            elif s[i][j] == s[i][j-1]-5:
                back[i][j] = "r"
            else:
                back[i][j] = "e"
                
    print(s[n][m])
    print(s)
    return back


def moves_to_strings(first_word, second_word, moves):
    pointer_w1 = 0
    pointer_w2 = 0
    print(moves)

    w1 = []
    w2 = []

    for move in moves:
        if move == "d":
            w1.append(first_word[pointer_w1])
            pointer_w1 += 1
            w2.append("-")
        if move == "r":
            w1.append("-")
            w2.append(second_word[pointer_w2])
            pointer_w2 += 1
        if move == "e":
            w1.append(first_word[pointer_w1])
            pointer_w1 += 1
            w2.append(second_word[pointer_w2])
            pointer_w2 += 1
        print(w1)
        print(w2)
        print()

    return "".join(w1), "".join(w2)
    

back = Manh(a,b)
print(back)
i = len(a)
j = len(b)
s = ""
while i>0 and j>0:
    s = back[i][j] + s
    
    if back[i][j] == "r":
        j = j-1
    elif back[i][j] == "e":
        i = i-1
        j= j-1
    else:
        i = i-1

st = moves_to_strings(a, b, s)
print(st[0])
print(st[1])
        
