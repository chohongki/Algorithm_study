# 백트래킹

N, M = map(int, input().split())

queue = []

def DFS(now):
    if len(queue) == M: 
        print(' '.join(map(str,queue)))
        return

    for i in range(now, N+1):
        queue.append(i)
        DFS(i)
        queue.pop()

DFS(1)