import sys
input = sys.stdin.readline

N = int(input())

node = [[] for _ in range(N+1)]

for _ in range(int(input())):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

queue = [1]
visited = set()
while queue:
    now = queue.pop()
    queue.extend(set(node[now])-visited)
    visited.add(now)
    
print(len(visited)-1)