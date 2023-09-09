fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba5b (1).txt", 'r')
unos = fp.read().splitlines()
n = int(unos[0].split()[0])
m = int(unos[0].split()[1])
down = [x.split() for x in unos[1:n+1]]
right = [x.split() for x in unos[n+2:]]
fp.close()

def Manhattan(n,m,down,right):
    s = []
    for i in range(n+1):
        s.append((m+1)*[0])
    
    for i in range(1,n+1):
        s[i][0] = (s[i-1][0] + int(down[i-1][0]))
    for j in range(1,m+1):
        s[0][j] = (s[0][j-1] + int(right[0][j-1]))
        
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j] = max(s[i][j-1]+int(right[i][j-1]),s[i-1][j]+int(down[i-1][j]))
    return s[n][m]

    
print(Manhattan(n,m,down,right))
