import sys
input = sys.stdin.readline

N = int(input())
arr = [0 for _ in range(10000001)]
for _ in range(N):
    arr[int(input())] += 1

for i in range(1, len(arr)):
    if arr[i]:
        for j in range(arr[i]): print(i)