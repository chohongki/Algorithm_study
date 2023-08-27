import sys
input = sys.stdin.readline


N, M = map(int, input().split())

table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

DP = [[0]*(N+1) for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        DP[i][j] = table[i-1][j-1] + DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(DP[x2][y2] - DP[x2][y1-1] - DP[x1-1][y2] + DP[x1-1][y1-1])
    