import sys
input = sys.stdin.readline

def makeSumTable(n):
    global table, DP, N
    if n:
        DP[n][n] = table[n][n] + DP[n-1][n] + DP[n][n-1] - DP[n-1][n-1]
        for i in range(n+1, N):
            DP[i][n] = table[i][n] + DP[i-1][n] + DP[i][n-1] - DP[i-1][n-1]
            DP[n][i] = table[n][i] + DP[n-1][i] + DP[n][i-1]- DP[n-1][i-1]
    else :
        for i in range(n+1, N):
            DP[i][n] = table[i][n] + DP[i-1][n]
            DP[n][i] = table[n][i] + DP[n][i-1]
    

N, M = map(int, input().split())

table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

DP = list(table)
for i in range(N):
    makeSumTable(i)

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1

    sum = DP[x2][y2] 

    if x1*y1 :
        sum += DP[x1-1][y1-1]
    if y1 :
        sum -= DP[x2][y1-1]
    if x1 :
        sum -= DP[x1-1][y2]
    print(sum)
    