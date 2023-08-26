#다익스트라 #djikstra

import heapq, sys

INF = sys.maxsize
input = sys.stdin.readline  #그지같네 이거 해야됨

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    
    graph[u].append((w, v))

def djikstra(graph, start):
    distances = [INF]*(V+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue
        
        for new_distance, new_destination  in graph[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, (distance, new_destination))

    return distances

distances = djikstra(graph, K)

for i in range(1, V+1):

    print("INF" if distances[i] == INF else distances[i])
