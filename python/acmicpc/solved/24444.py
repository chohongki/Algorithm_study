from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

cnt = 1
visited = [0]*(N+1)
queue = deque([R])

while queue:
    i = queue.popleft()
    if visited[i]: continue
    visited[i] = cnt
    cnt += 1
    queue.extend(graph[i])

print("\n".join(str(i) for i in visited[1:]))