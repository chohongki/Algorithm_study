from collections import deque

def DFS(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            temp = list(set(graph[n]) - set(visited))
            temp.sort(reverse=True)
            stack += temp
    
    return " ".join(str(i) for i in visited)

def BFS(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            temp = list(set(graph[n]) - set(visited))
            temp.sort()
            queue += temp

    return " ".join(str(i) for i in visited)
    

# N : 정점 갯수, M : 노드 갯수, V : 시작점
N, M, V = list(map(lambda x: int(x), input().split()))

graph = {i+1 : [] for i in range(N)}

for i in range(M):
    s, e = list(map(lambda x: int(x), input().split()))
    if e not in graph[s]:
        graph[s].append(e)
    if s not in graph[e]:
        graph[e].append(s)

print(DFS(graph, V))
print(BFS(graph, V))