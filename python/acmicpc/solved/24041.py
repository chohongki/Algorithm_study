# 이진탐색, 그리디, 정렬

import sys
input = sys.stdin.readline

N, G, K = map(int, input().split())

lst = [[], []]

def calc_germ(l, x):
    return [(speed * max(1, x-limit)) for speed, limit in l]

def get_g(x):
    res = sum(calc_germ(lst[0], x))
    germ_noncrucial = calc_germ(lst[1], x)
    germ_noncrucial.sort(reverse=True)
    res += sum(germ_noncrucial[K:])
    return res

for _ in range(N):
    a, b, c = map(int, input().split())
    lst[c].append((a, b))

res = 0
left, right = 1, int(2e9)
while left <= right:
    mid = (left + right) // 2
    if get_g(mid) <= G:
        res = mid
        left = mid + 1
    else :
        right = mid - 1
        
print(res)
