import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
boat = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    l, r = map(int, input().split())
    boat[l-1][r-1] = 1

cnt = 0
for l1, l2 in combinations(range(N), 2):
    for r1, r2 in combinations(range(N), 2):
        if boat[l1][r1]+boat[l2][r1]+boat[l1][r2]+boat[l2][r2] == 4:
            cnt += 1
print(cnt)