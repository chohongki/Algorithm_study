import sys
from decimal import Decimal
input = sys.stdin.readline

N, K = map(int, input().split())

lst = []

for _ in range(N):
    i, c, h = map(int, input().split())
    lst.append((Decimal(h)/Decimal(c), c, i))

lst.sort(key=lambda x:(-x[0], x[1], x[2]))

for v, c, i in lst[:K]:
    print(i)
    