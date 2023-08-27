A, B = map(int,input().split())

big = 10000000

flag = True

def dfs(num, cnt):
    if num > B :
        return 10000000
    elif num == B:
        return cnt
    else:
        return min(dfs(num*2, cnt+1), dfs(num * 10 + 1, cnt+1))

res = dfs(A, 1)

if res == big:
    print(-1)
else :
    print(res)