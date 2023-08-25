# MST : 1. Prim Algorithm -> O(E logV)
# https://lotuslee.tistory.com/46
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
        print(now_node)
        visitied[now_node] = 1
        sum += now_value
        cnt += 1
        for i in graph[now_node]:
            heapq.heappush(queue, i)

    return sum

# MST : 2. Kruskal Algorithm
# https://ozofweird.tistory.com/entry/%EA%B0%9C%EB%85%90-%ED%95%99%EC%8A%B5-%EB%B0%8F-%EC%A0%95%EB%A6%AC-%EA%B8%B0%EC%B4%88-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%B5%9C%EC%86%8C-%EC%8B%A0%EC%9E%A5-%ED%8A%B8%EB%A6%AC

def kruskal():
    return

import sys
input = sys.stdin.readline

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

print(prim())

