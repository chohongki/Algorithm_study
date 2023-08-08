import sys

N = int(input())

lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))

s = 0
tmp = 0
lst.sort(key=lambda x:(x[0], x[1]))
for i in range(N):
    x, y = lst[i]
    if i%2:
        s += y - tmp
    else:
        tmp = y
lst.sort(key=lambda x:(x[1], x[0]))
for i in range(N):
    x, y = lst[i]
    if i%2:
        s += x - tmp
    else:
        tmp = x
print(s)