import sys
input = sys.stdin.readline

N, K = map(int, input().split())
L = [[0, 0]]
for _ in range(N):
    L.append(list(map(int, input().split())))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    weight, price = L[i]
    for j in range(1, K+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(price + dp[i-1][j-weight], dp[i-1][j])

print(dp[-1][-1])