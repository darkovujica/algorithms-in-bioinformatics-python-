fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba5c (3).txt", 'r')
unos = fp.read().splitlines()
a = unos[0]
b = unos[1]
fp.close()

def Manh(a,b):
    n = len(a)
    m= len(b)
    s = []
    back = []
    for i in range(n+1):
        s.append((m+1)*[0])
        back.append((m+1)*[0])

    for i in range(n+1):
        s[i][0] = 0
    for i in range(m+1):
        s[0][i] = 0
        
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j] = max(s[i][j-1],s[i-1][j]) 
            if a[i-1] == b[j-1]:
                s[i][j] = max(s[i][j],s[i-1][j-1]+1)

            if s[i][j] == s[i-1][j]:
                back[i][j] = "d"
            elif s[i][j] == s[i][j-1]:
                back[i][j] = "r"
            elif s[i][j] == s[i-1][j-1]+1 and a[i-1]==b[j-1]:
                back[i][j] = "e"        
    return back


#def Output(i,j,string):
#    if i==0 or j==0:
#        print(string)
#        
#    elif back[i][j] == "d":
#        Output(i-1,j,string)
#    elif back[i][j] == "r":
#        Output(i,j-1,string)
#    else:
#         Output(i-1,j-1, a[i-1] + string)
# output javlja grešku u smislu prevelike dubine rekurzije
    

back = Manh(a,b)

i = len(a)
j = len(b)
s = ""
while i>0 and j>0:
    if back[i][j] == "r":
        j = j-1
    elif back[i][j] == "e":
        s = a[i-1] + s
        i = i-1
        j= j-1
    else:
        i = i-1
print(s)
        
