import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    lines = []
    lines.append(list(map(int, input().split())))
    lines.append(list(map(int, input().split())))
    lines[0].extend([0,0])
    lines[1].extend([0,0])

    DP = list(lines)
    DP[0][1] = lines[0][1] + DP[1][0]
    DP[1][1] = lines[1][1] + DP[0][0]

    for i in range(2, n+1):
        DP[0][i] = lines[0][i] + max(DP[1][i-1], DP[1][i-2])
        DP[1][i] = lines[1][i] + max(DP[0][i-1], DP[0][i-2])

    print(max(DP[0][n], DP[1][n]))