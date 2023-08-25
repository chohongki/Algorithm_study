import sys
import heapq
input = sys.stdin.readline

n = int(input())
lst = [[] for _ in range(51)]
max_len = -1
for _ in range(n):
    s = input().replace('\n','')
    l = len(s)
    lst[l].append(s)

for l in lst:
    if l:
        l=sorted(list(set(l)))
        print('\n'.join(l))