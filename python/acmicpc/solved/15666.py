N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()

res = []

def test(depth):
    if depth >= M:
        print(' '.join(res))
        return

    for i in range(len(nums)):
        if depth>0 and int(res[-1]) > nums[i]:
            continue
        res.append(str(nums[i]))
        test(depth+1)
        res.pop(-1)

test(0)