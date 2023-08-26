import math

m = int(input())
n = list(map(lambda x : int(x), input().split()))
k = int(input())

percent=0
tot = math.comb(sum(n),k)
for i in range(m):
    percent += math.comb(n[i],k)/tot

print(percent)