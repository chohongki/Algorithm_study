import sys
input = sys.stdin.readline

N, C = map(int, input().split())

home = [int(input()) for _ in range(N)]
home.sort()

s, e = 1, home[-1] - home[0]
res = 0
while s <= e:
    cnt = 1
    space = (e + s) // 2
    place = home[0]
    for i in range(1, N):
        if home[i] - place >= space:
            cnt += 1
            place = home[i]
    if cnt >= C:
        s = space + 1
        res = space
    elif cnt < C:
        e = space - 1
print(res)