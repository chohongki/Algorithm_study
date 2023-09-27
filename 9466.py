from collections import deque

def dfs(students, r):
    queue = deque()
    visited = set()
    
    queue.append(students[r-1])
    while queue:
        now = queue.popleft()

        if now in visited:
            continue

        if now == r:
            return visited
        
        queue.append(students[now-1])

    return set()

def test():
    N = int(input())
    students = list(map(int, input().split()))
    
    remain = set(range(1, N+1))
    for i in range(1, N+1):
        if i in remain:
            remain = remain - dfs(students, i)
    print(list(remain))



T = int(input())

for _ in range(T):
    test()