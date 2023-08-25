from itertools import combinations

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

for i in sorted(list(set(combinations(nums, M)))):
    print(' '.join(map(str,i)))
