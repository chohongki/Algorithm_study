N, M = map(int, input().split())

nums = sorted(list(set(map(int, input().split()))))

res = []
def func(depth):
    if depth == M:
        print(' '.join(map(str,res)))
        return
    
    for i in nums:
        res.append(i)
        func(depth+1)
        res.pop()

func(0)
