N = int(input())

steps = []
for _ in range(N):
    steps.append(int(input()))

res = [[steps[i], 0] for i in range(N)]

if N >= 2:
    res[1][1] = steps[1] + res[0][0]
    for i in range(2, N):
        res[i][0] = steps[i] + max(res[i-2])
        res[i][1] = steps[i] + res[i-1][0]

print(max(res[N-1]))