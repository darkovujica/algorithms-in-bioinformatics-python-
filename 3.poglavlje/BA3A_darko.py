k = int(input())
text = input()

lista=[]
for i in range(len(text)-k+1):
    lista.append(text[i:i+k])
    
lista.sort()
#for l in lista:
#    print(l)

fp = open("C:\\Users\\DARKO\\Downloads\\BA3A.txt", 'w')
for l in lista:
    fp.write(l + "\n")
fp.close()
