# 백트래킹

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
queue = []

def DFS(now):
    if len(queue) == M: 
        print(' '.join(map(str,queue)))
        return

    for i in nums:
        if i not in queue:
            queue.append(i)
            DFS(i)
            queue.pop()

DFS(nums[0])