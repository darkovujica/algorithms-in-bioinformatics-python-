Text = input()
k = int(input())

def Count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count = count + 1
    return count

def FrequencyList(text, k):
    l = []
    broj = []
    for i in range(len(text) - k + 1):
        q = Count(text, text[i : i + k])
        l.append(q)
    return l 
    
l = FrequencyList(Text, k)
M = max(l)
F = []

for i in range(len(Text) - k + 1):
    q = l[i]
    rijec = Text[i : i + k]
    if(q == M and rijec not in F):
        print(rijec + " ")
    F.append(rijec)
