import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    u, v, distance = map(int, input().split())
    graph[u].append((v, distance))
    graph[v].append((u, distance))

v1, v2 = map(int, input().split())

def djikstra(start):
    global graph
    distances = [INF]*(N+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (start, 0))

    while queue:
        current_destination, current_distance = heapq.heappop(queue)

        if current_distance > distances[current_destination]:
            continue

        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, (new_destination, distance))

    return distances

case1 = djikstra(1) # 1에서 출발
case2 = djikstra(v1)    # v1에서 출발
case3 = djikstra(v2)    # v2에서 출발

res = min(case1[v1]+case2[v2]+case3[N], case1[v2]+case3[v1]+case2[N])

if res >= INF:
    print(-1)
else : 
    print(res)