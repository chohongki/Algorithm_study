import sys

input = sys.stdin.readline

N = int(input())

nums = []

for _ in range(N):
    nums.append(int(input()))

nums.sort()

if N < 3:
    if N == 1: 
        sums = [0]
        sums[0] = nums[0]
    if N == 2: 
        sums = [0, 0]
        sums[0] = max(nums[0]+nums[1],nums[0]*nums[1])


else:
    sums = [-2**32]*N
    sums[-1] = nums[-1]
    sums[-2] = max(nums[-1]+nums[-2], nums[-1]*nums[-2])

    def greedy(i):
        if i == N-1 or i == N-2: return nums[N-1]
        sums[i] = max(sums[i+1]+nums[i], sums[i+2]+nums[i]*nums[i+1])
        return sums[i]

    for i in range(N-3, -1, -1):
        greedy(i)

print(sums[0])