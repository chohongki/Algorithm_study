N = int(input())
Ai = list(map(int, input().split()))

countlist = [1 for i in range(N)]

for i in range(1, N):
    for j in range(i):
        if Ai[i] < Ai[j] and countlist[i] <= countlist[j]:
            countlist[i] = countlist[j] + 1

print(max(countlist))