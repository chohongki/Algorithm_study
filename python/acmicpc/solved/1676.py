import math

N = int(input())
a = str(math.factorial(N))

cnt = 0
for i in range(1, len(a)+1):
    if a[-i] != '0':
        break
    else : cnt += 1

print(cnt)