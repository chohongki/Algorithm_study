import sys
input = sys.stdin.readline

n = int(input())
queue = []
max = -1
max_n = 0
for _ in range(n):
    l = list(map(int, input().split()))
    if len(l)==2:
        queue.append(l[1])
    else:
        queue.pop(0)
    L = len(queue)
    if L>max:
        max = L
        max_n = queue[-1]
    elif L == max:
        if queue[-1] < max_n:
            max_n = queue[-1]

print(max, max_n)

