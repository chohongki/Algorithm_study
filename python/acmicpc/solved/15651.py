# 백트래킹

N, M = map(int, input().split())

queue = []

def DFS():
    if len(queue) == M: 
        print(' '.join(map(str,queue)))
        return

    for i in range(1, N+1):
        queue.append(i)
        DFS()
        queue.pop()

DFS()