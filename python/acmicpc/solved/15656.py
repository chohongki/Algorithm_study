# 백트래킹

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
queue = []

def DFS():
    if len(queue) == M: 
        print(' '.join(map(str,queue)))
        return

    for i in range(len(nums)):
        queue.append(nums[i])
        DFS()
        queue.pop()

DFS()