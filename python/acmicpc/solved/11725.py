import sys
input = sys.stdin.readline

N = int(input())

dic = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

'''풀이 1'''
res = [0 for _ in range(N+1)]
queue = [1]
visited = set()
while queue:
    now = queue.pop()
    visited.add(now)
    go = set(dic[now])-visited
    queue.extend(go)
    for i in go:
        res[i] = now

for i in res[2:]:
    print(i)