import sys
input = sys.stdin.readline

N, M = map(int, input().split())


sys.setrecursionlimit(M+1)
graph = {}

for _ in range(M):
    A, B = map(int, input().split())
    try:
        graph[B].append(A)
    except:
        graph[B] = [A]

X = int(input())
queue = set()

def search(n):
    try:
        if n not in queue:
            for i in graph[n]:
                search(i)
                queue.add(i)
    except:
        return

search(X)

print(len(queue))