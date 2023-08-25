# 9진법

n = input()
L = len(n)
res = 0

n = int(n)
for i in range(L):
    now = n % 10
    n //= 10
    if now > 4:
        res += (now-1)*(9**i)
    else :
        res += now*(9**i)

print(res)
