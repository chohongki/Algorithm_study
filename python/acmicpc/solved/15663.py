from itertools import permutations

N, M = map(int, input().split())

nums = list(map(int, input().split()))

for i in sorted(list(set(permutations(nums, M)))):
    print(' '.join(map(str,i)))
