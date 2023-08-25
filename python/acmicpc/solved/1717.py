# union-find

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

lst = [i for i in range(n+2)]

def find(x):
    if lst[x] == x:
        return x
    else:
        lst[x] = find(lst[x])
        return lst[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    elif x < y:
        lst[y] = x
    else:
        lst[x] = y

for _ in range(m):
    t, a, b = map(int, input().split())
    if t:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)