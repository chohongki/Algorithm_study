# 백트래킹

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
queue = []

def DFS(now):
    if len(queue) == M: 
        print(' '.join(map(str,queue)))
        return

    for i in range(now, len(nums)):
        if nums[i] not in queue:
            queue.append(nums[i])
            DFS(i+1)
            queue.pop()

DFS(0)