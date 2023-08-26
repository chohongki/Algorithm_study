n = int(input())

lst = list(map(int,input().split()))

min = 10000000
max = 1

for i in range(n):
    min = min if min<lst[i] else lst[i]
    max = max if max>lst[i] else lst[i]

print(min*max)
