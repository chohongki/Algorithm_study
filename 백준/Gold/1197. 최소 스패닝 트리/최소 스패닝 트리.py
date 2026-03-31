def prim():
    import heapq
    global V

    sum = 0
    cnt = 0
    queue = [[0, 1]]
    visitied = [0 for _ in range(V+1)]
    while queue:
        if cnt >= V: 
            break
        now_value, now_node = heapq.heappop(queue)
        if visitied[now_node]: 
            continue
        visitied[now_node] = 1
        sum += now_value
        cnt += 1
        for i in graph[now_node]:
            heapq.heappush(queue, i)

    return sum

import sys
input = sys.stdin.readline

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

print(prim())
