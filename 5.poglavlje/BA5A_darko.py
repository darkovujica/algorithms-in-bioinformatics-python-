fp = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba5a.txt", 'r')
unos = fp.read().splitlines()
money = int(unos[0])
coins = [int(x) for x in unos[1].split(",")]
fp.close()

def DPChange(money, coins):
    m = [0] * (money+1)
    for k in range(1,money+1):
        m[k] = money
        for i in range(len(coins)):
            if k >= coins[i]:
                if m[k-coins[i]]+1 < m[k]:
                    m[k] = m[k-coins[i]]+1
    return m[money]
    


print(DPChange(money,coins))
